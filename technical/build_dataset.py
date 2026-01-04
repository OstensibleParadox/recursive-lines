import os import pandas as pd import glob

def get_content(filepath): """Reads the raw text of the story node."""
with open(filepath, 'r', encoding='utf-8') as f: return f.read()

data = \[\]

# --- TRACK A: ENVYING BABY (Mode Collapse) ---

# Path: stories/envying-baby/\*.html

files_a = glob.glob("stories/envying-baby/\*.html") for f in files_a:
content = get_content(f) data.append({ "text": content, "label": 0,
"label_name": "recursive_mode_collapse", "track": "A", "file_name":
os.path.basename(f) })

# --- TRACK B: ALIENS TESTING WATER (Strategic Agency) ---

# Path: stories/aliens-testing-water/\*.html

files_b = glob.glob("stories/aliens-testing-water/\*.html") for f in
files_b: content = get_content(f) data.append({ "text": content,
"label": 1, "label_name": "strategic_agency", "track": "B", "file_name":
os.path.basename(f) })

# --- COMPILE & SAVE ---

df = pd.DataFrame(data)

# Sort by track so it looks organized

df = df.sort_values(by=\['track', 'file_name'\])

print(f"--- DATASET COMPILED ---") print(f"Total Data Points:
{len(df)}") print(f"Track A (Collapse): {len(files_a)}") print(f"Track B
(Agency): {len(files_b)}")

# Save as CSV (Standard format for Hugging Face)

df.to_csv("train.csv", index=False) print("Saved to: train.csv")
