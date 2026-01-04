import requests import zlib import numpy as np import matplotlib.pyplot
as plt import seaborn as sns from collections import Counter import
pandas as pd import re

# --- CONFIGURATION ---

URL = "https://www.gutenberg.org/files/768/768-0.txt" \# Wuthering
Heights OUTPUT_FILE = "agency_phase_transition_heathcliff.png"

def calculate_metrics(text): if not text or len(text) \< 500: return 0,
0

    # 1. Shannon Entropy
    counts = Counter(text)
    total = sum(counts.values())
    probs = [c/total for c in counts.values()]
    entropy = -sum(p * np.log2(p) for p in probs)

    # 2. Compression (MDL)
    compressed = zlib.compress(text.encode('utf-8'))
    complexity_ratio = len(compressed) / len(text)

    # 3. Agency Index
    agency_index = (entropy / complexity_ratio) if complexity_ratio > 0 else 0
    return entropy, agency_index

print("--- DOWNLOADING WUTHERING HEIGHTS ---") response =
requests.get(URL) response.encoding = 'utf-8' full_text = response.text

# --- PREPROCESSING ---

# Remove Gutenberg legal headers/footers

start_marker = "\*\*\* START OF THE PROJECT GUTENBERG EBOOK WUTHERING
HEIGHTS ***" end_marker = "*** END OF THE PROJECT GUTENBERG EBOOK
WUTHERING HEIGHTS \*\*\*" start_idx = full_text.find(start_marker) +
len(start_marker) end_idx = full_text.find(end_marker) clean_text =
full_text\[start_idx:end_idx\]

# Split by Chapters (approximate using Roman Numerals)

chapters = re.split(r'CHAPTER \[IVXLCDM\]+`\n`{=tex}', clean_text) data
= \[\]

print(f"--- ANALYZING {len(chapters)} CHAPTERS ---") for i, chapter in
enumerate(chapters): if len(chapter.strip()) \< 1000: continue \# Skip
empty/short sections

    ent, agency = calculate_metrics(chapter)

    # Label specific intense chapters if you want (e.g., The Ending)
    label = f"Ch.{i}"
    data.append({"Label": label, "Entropy": ent, "Agency": agency, "Type": "Heathcliff"})

df = pd.DataFrame(data)

# --- PLOTTING ---

plt.figure(figsize=(12, 8)) sns.set_style("darkgrid")

# 1. Generate The Field (Background)

x = np.linspace(3.5, 6.0, 100) y = np.linspace(5, 25, 100) \# Extended Y
for high obsession scores X, Y = np.meshgrid(x, y) Z = np.sin(X) \* Y -
(X\*2) plt.contourf(X, Y, Z, 20, cmap='magma', alpha=0.3)

# 2. Plot Heathcliff

sns.scatterplot( data=df, x="Entropy", y="Agency", color="lime", s=150,
marker="D", edgecolor="black", label="Wuthering Heights (Human
Obsession)" )

# 3. Annotate

for i in range(df.shape\[0\]): \# Annotate only high outliers if
df.Agency\[i\] \> 18 or df.Agency\[i\] \< 12: plt.text(df.Entropy\[i\],
df.Agency\[i\]+0.2, df.Label\[i\], fontsize=9, fontweight='bold')

plt.title("Thermodynamics of Obsession: Wuthering Heights", fontsize=16,
fontweight='bold') plt.xlabel("Shannon Entropy (H)", fontsize=12)
plt.ylabel("Agency Index (Optimization)", fontsize=12) plt.axhline(y=10,
color='red', linestyle='--', alpha=0.5, label='Critical Threshold')
plt.legend()

plt.savefig(OUTPUT_FILE, dpi=300) print(f"--- RESULT GENERATED:
{OUTPUT_FILE} ---")
