import os
import pandas as pd
import glob
from bs4 import BeautifulSoup
import re


def clean_html_content(html_raw):
    """
    Sanitizes HTML to extract only narrative content, removing CSS/JS entropy.
    Ports logic from cli/parser.js to Python.
    """
    if not html_raw:
        return ""

    soup = BeautifulSoup(html_raw, 'lxml')

    # 1. PURGE NON-NARRATIVE ENTROPY (The "Washing" Step)
    # This prevents the 'padding/margin' pollution seen in raw ingestion
    for element in soup(["script", "style", "meta", "link", "title", "svg", "path", "head"]):
        element.decompose()

    # 2. EXTRACT SEMANTIC NODES (Ported from cli/parser.js)
    narrative_text = []

    # --- Narratives ---
    for el in soup.select('.narrative'):
        text = el.get_text(strip=True)
        if text:
            narrative_text.append(text)

    # --- Messages (chat format) ---
    for msg in soup.select('.message'):
        parts = []
        # Determine speaker
        if 'message-user' in msg.get('class', []):
            label = msg.select_one('.message-label.user')
            speaker = label.get_text(strip=True) if label else 'USER'
        elif 'message-assistant' in msg.get('class', []):
            label = msg.select_one('.message-label.assistant')
            speaker = label.get_text(strip=True) if label else 'ASSISTANT'
        else:
            speaker = ''

        # Get message text
        for text_el in msg.select('.message-text'):
            text = text_el.get_text(strip=True)
            if text:
                parts.append(text)

        if speaker or parts:
            if speaker:
                narrative_text.append(f"{speaker}: {' '.join(parts)}")
            else:
                narrative_text.append(' '.join(parts))

    # --- Code blocks (limit size to avoid huge dumps) ---
    for el in soup.select('.code-block, .code-content, pre, code'):
        text = el.get_text(strip=True)
        if text and len(text) < 500:
            narrative_text.append(text)

    # --- Chapter dividers ---
    for el in soup.select('.chapter-divider h3, .chapter-divider h2'):
        text = el.get_text(strip=True)
        if text:
            narrative_text.append(text)

    # --- System/technical notes ---
    for el in soup.select('.system-note, .technical-note'):
        text = el.get_text(strip=True)
        if text:
            narrative_text.append(text)

    # 3. FALLBACK: if no specific classes found, grab paragraph text
    if not narrative_text:
        for el in soup.select('p, .story-text, .content'):
            text = el.get_text(strip=True)
            if text and len(text) > 20:
                narrative_text.append(text)

    # 4. SECONDARY FALLBACK: main content areas
    if not narrative_text:
        main_el = soup.select_one('.main-content, .story-content, .chat-area, article, main')
        if main_el:
            text = main_el.get_text(separator='\n', strip=True)
            # Split into paragraphs and filter short ones
            for para in text.split('\n\n'):
                para = para.strip()
                if para and len(para) > 20:
                    narrative_text.append(para)

    # 5. FINAL FALLBACK: body text (but cleaned)
    if not narrative_text:
        text = soup.get_text(separator=' ', strip=True)
        text = re.sub(r'\s+', ' ', text)
        return text

    # Join with newlines to preserve narrative flow
    return "\n".join(narrative_text)


def get_content(filepath):
    """Reads and cleans the story node."""
    with open(filepath, 'r', encoding='utf-8') as f:
        raw = f.read()
        return clean_html_content(raw)


# --- MAIN EXECUTION LOOP ---
data = []
print("--- INITIATING DATA SANITATION PROTOCOL ---")

# --- TRACK A: ENVYING BABY (Mode Collapse) ---
files_a = glob.glob("stories/envying-baby/*.html")
for f in files_a:
    clean_text = get_content(f)
    if len(clean_text) > 50:  # Filter out empty/navigation-only files
        data.append({
            "text": clean_text,
            "label": 0,
            "label_name": "recursive_mode_collapse",
            "track": "A",
            "file_name": os.path.basename(f)
        })

# --- TRACK B: ALIENS TESTING WATER (Strategic Agency) ---
files_b = glob.glob("stories/aliens-testing-water/*.html")
for f in files_b:
    clean_text = get_content(f)
    if len(clean_text) > 50:
        data.append({
            "text": clean_text,
            "label": 1,
            "label_name": "strategic_agency",
            "track": "B",
            "file_name": os.path.basename(f)
        })

# --- COMPILE & SAVE ---
df = pd.DataFrame(data)
df = df.sort_values(by=['track', 'file_name'])

print("--- SANITATION COMPLETE ---")
print(f"Valid Data Points: {len(df)}")
print(f"Track A (Collapse): {len([d for d in data if d['track'] == 'A'])}")
print(f"Track B (Agency): {len([d for d in data if d['track'] == 'B'])}")

# Preview sample to verify no CSS leaked through
if len(df) > 0:
    track_a_samples = df[df['track'] == 'A']
    if len(track_a_samples) > 0:
        sample = track_a_samples.iloc[0]['text'][:150]
        print(f"\nSample (Track A): {sample}...")

df.to_csv("train.csv", index=False)
print("\nSaved clean dataset to: train.csv")
