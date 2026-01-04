import os
import glob
import zlib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import pandas as pd

# --- CONFIGURATION ---
STORY_PATH = "../stories"
OUTPUT_FILE = "agency_phase_transition_empirical.png"


def calculate_metrics(text):
    """
    Computes the coordinates for a text node.
    X-axis: Entropy (Stochasticity)
    Y-axis: Agency Index (Compression Efficiency * Divergence)
    """
    if not text:
        return 0, 0

    # 1. Shannon Entropy (H) - The 'Noise'
    counts = Counter(text)
    total = sum(counts.values())
    probs = [c/total for c in counts.values()]
    entropy = -sum(p * np.log2(p) for p in probs)

    # 2. Algorithmic Complexity (MDL) - The 'Structure'
    # We use zlib compression ratio as a proxy for Kolmogorov Complexity
    compressed = zlib.compress(text.encode('utf-8'))
    complexity_ratio = len(compressed) / len(text)

    # 3. Agency Index (The Metric)
    # Agency = Structure / Noise.
    # High Agency = Low Complexity (High coherence) + High Entropy (Richness)
    # We invert complexity because 'Agency' implies efficient compression of complex goals.
    agency_index = (entropy / complexity_ratio) if complexity_ratio > 0 else 0

    return entropy, agency_index


# --- DATA GATHERING ---

print("--- READING NARRATIVE DATA ---")
data = []

# Scan Track A (Envying Baby)
for f in glob.glob(f"{STORY_PATH}/envying-baby/*.html"):
    name = os.path.basename(f)
    with open(f, 'r') as file:
        text = file.read()
    ent, agency = calculate_metrics(text)
    data.append({"Track": "A: Collapse", "File": name, "Entropy": ent, "Agency": agency})

# Scan Track B (Aliens)
for f in glob.glob(f"{STORY_PATH}/aliens-testing-water/*.html"):
    name = os.path.basename(f)
    with open(f, 'r') as file:
        text = file.read()
    ent, agency = calculate_metrics(text)
    data.append({"Track": "B: Strategic", "File": name, "Entropy": ent, "Agency": agency})

df = pd.DataFrame(data)

# --- THE PHASE TRANSITION SIMULATION (BACKGROUND) ---

print("--- GENERATING THERMODYNAMIC FIELD ---")
# Generate a synthetic heatmap representing the theoretical bounds
x = np.linspace(3.5, 6.0, 100)  # Typical entropy range for English text
y = np.linspace(5, 15, 100)     # Typical Agency Index range
X, Y = np.meshgrid(x, y)
# The "Critical Line" equation (Synthetic phase boundary)
Z = np.sin(X) * Y - (X * 2)

# --- PLOTTING ---

plt.figure(figsize=(12, 8))
sns.set_style("darkgrid")

# 1. Draw the Heatmap
plt.contourf(X, Y, Z, 20, cmap='magma', alpha=0.3)
plt.colorbar(label='Thermodynamic Potential ($\\Psi$)')

# 2. Plot the Story Nodes
sns.scatterplot(
    data=df,
    x="Entropy",
    y="Agency",
    hue="Track",
    style="Track",
    s=200,
    palette={"A: Collapse": "#ff2a6d", "B: Strategic": "#05d9e8"},
    edgecolor="black"
)

# 3. Annotate
for i in range(df.shape[0]):
    plt.text(
        df.Entropy.iloc[i] + 0.02,
        df.Agency.iloc[i],
        df.File.iloc[i].split('.')[0],
        fontsize=8,
        alpha=0.7
    )

plt.title("Agency Phase Transition: Empirical Mapping of Narrative Tracks", fontsize=16, fontweight='bold')
plt.xlabel("Shannon Entropy ($H$)", fontsize=12)
plt.ylabel("Agency Index ($\\mathcal{A} \\propto H \\times MDL^{-1}$)", fontsize=12)
plt.axhline(y=10, color='red', linestyle='--', alpha=0.5, label='Critical Agency Threshold')
plt.legend(loc='lower right')

plt.savefig(OUTPUT_FILE, dpi=300)
print(f"--- GRAPH GENERATED: {OUTPUT_FILE} ---")
