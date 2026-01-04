#!/usr/bin/env python3
"""
===========================================
NARRATIVE ANALYSIS PIPELINE
===========================================

This is your ONE entry point. Instead of running 6 scripts manually,
you run this ONE script and pick what you want:

    python run_pipeline.py --all           # Run everything
    python run_pipeline.py --simulation    # Just the agent simulation
    python run_pipeline.py --analyze       # Just analyze stories
    python run_pipeline.py --dataset       # Just build the CSV dataset

Settings are in config.yaml - edit that file, not the Python code.
"""

import argparse
import yaml
import os
import sys
from pathlib import Path

# Make sure we're running from the technical/ directory
SCRIPT_DIR = Path(__file__).parent.resolve()
os.chdir(SCRIPT_DIR)


def load_config():
    """Load settings from config.yaml"""
    config_path = SCRIPT_DIR / "config.yaml"
    if not config_path.exists():
        print("ERROR: config.yaml not found!")
        print("Make sure you're running from the technical/ folder.")
        sys.exit(1)

    with open(config_path) as f:
        return yaml.safe_load(f)


def ensure_output_dir(config):
    """Create results folder if it doesn't exist"""
    results_dir = Path(config['output']['results_dir'])
    results_dir.mkdir(exist_ok=True)
    return results_dir


def run_simulation(config):
    """
    Run the agency phase transition simulation.
    This generates the big heatmap showing how "agency" emerges
    from the balance of intent vs randomness.
    """
    print("\n" + "="*50)
    print("RUNNING: Agent Simulation")
    print("="*50)

    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    from scipy.ndimage import gaussian_filter
    from multiprocessing import Pool

    # Pull settings from config
    sim = config['simulation']
    GRID_SIZE = sim['grid_size']
    STEPS = sim['steps']
    TRIALS = sim['trials_per_param']
    RESOLUTION = sim['resolution']

    BIAS_RANGE = np.linspace(0, 1.0, RESOLUTION)
    NOISE_RANGE = np.linspace(0.1, 1.0, RESOLUTION)

    def run_one_simulation(args):
        bias_strength, noise_level = args
        target = np.array([GRID_SIZE // 2, GRID_SIZE // 2])
        pos = np.array([np.random.randint(0, GRID_SIZE),
                        np.random.randint(0, GRID_SIZE)], dtype=float)
        trajectory = [pos.copy()]

        for _ in range(STEPS):
            direction = target - pos
            norm = np.linalg.norm(direction)
            strategic = direction / norm if norm > 0 else np.array([0, 0])
            random = np.random.randn(2)

            step = (bias_strength * strategic) + (noise_level * random)
            pos = np.clip(pos + step, 0, GRID_SIZE - 1)
            trajectory.append(pos.copy())

        trajectory = np.array(trajectory)

        # Calculate agency metrics
        displacement = np.linalg.norm(trajectory[-1] - trajectory[0])
        total_dist = np.sum(np.linalg.norm(np.diff(trajectory, axis=0), axis=1))
        efficiency = displacement / (total_dist + 1e-9)

        vectors = np.diff(trajectory, axis=0)
        angles = np.arctan2(vectors[:, 1], vectors[:, 0])
        complexity = np.sum(np.abs(np.diff(angles))) + 1e-9

        return (efficiency * 100) / (np.log(complexity) + 1)

    print(f"Resolution: {RESOLUTION}x{RESOLUTION}")
    print(f"Trials per point: {TRIALS}")
    print(f"Total simulations: {RESOLUTION * RESOLUTION * TRIALS}")

    # Build parameter grid
    params = [(b, n) for b in BIAS_RANGE for n in NOISE_RANGE for _ in range(TRIALS)]

    # Run in parallel
    with Pool() as p:
        results = p.map(run_one_simulation, params)

    # Reshape and average
    results = np.array(results).reshape(RESOLUTION, RESOLUTION, TRIALS)
    mean_agency = gaussian_filter(np.mean(results, axis=2), sigma=0.8)

    # Plot
    plt.figure(figsize=(10, 8))
    sns.set_theme(style="white")
    ax = sns.heatmap(mean_agency, cmap="inferno",
                     cbar_kws={'label': 'Agency Index'})

    ticks = np.linspace(0, RESOLUTION-1, 6)
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.set_xticklabels(np.round(np.linspace(0.1, 1.0, 6), 1))
    ax.set_yticklabels(np.round(np.linspace(0.0, 1.0, 6), 1))
    ax.invert_yaxis()

    plt.title("Agency Phase Transition", fontsize=14, weight='bold')
    plt.xlabel("Environmental Noise")
    plt.ylabel("Strategic Bias (Intent)")

    output_path = ensure_output_dir(config) / "agency_phase_transition.png"
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"✓ Saved: {output_path}")


def run_story_analysis(config):
    """
    Analyze the story files using entropy and compression metrics.
    Plots where each story falls on the "agency" spectrum.
    """
    print("\n" + "="*50)
    print("RUNNING: Story Analysis")
    print("="*50)

    import glob
    import zlib
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    import pandas as pd
    from collections import Counter

    def calculate_metrics(text):
        if not text:
            return 0, 0
        counts = Counter(text)
        total = sum(counts.values())
        probs = [c/total for c in counts.values()]
        entropy = -sum(p * np.log2(p) for p in probs)

        compressed = zlib.compress(text.encode('utf-8'))
        complexity = len(compressed) / len(text)

        agency = entropy / complexity if complexity > 0 else 0
        return entropy, agency

    data = []

    # Track A
    track_a_path = config['stories']['track_a']
    for f in glob.glob(f"{track_a_path}/*.html"):
        with open(f) as file:
            text = file.read()
        ent, agency = calculate_metrics(text)
        data.append({"Track": "A: Collapse", "File": Path(f).stem,
                     "Entropy": ent, "Agency": agency})

    # Track B
    track_b_path = config['stories']['track_b']
    for f in glob.glob(f"{track_b_path}/*.html"):
        with open(f) as file:
            text = file.read()
        ent, agency = calculate_metrics(text)
        data.append({"Track": "B: Strategic", "File": Path(f).stem,
                     "Entropy": ent, "Agency": agency})

    if not data:
        print("WARNING: No story files found! Check paths in config.yaml")
        return

    df = pd.DataFrame(data)
    print(f"Found {len(data)} story files")

    # Plot
    plt.figure(figsize=(12, 8))
    sns.set_style("darkgrid")

    # Background field
    x = np.linspace(3.5, 6.0, 100)
    y = np.linspace(5, 15, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(X) * Y - (X * 2)
    plt.contourf(X, Y, Z, 20, cmap='magma', alpha=0.3)

    # Story points
    sns.scatterplot(data=df, x="Entropy", y="Agency", hue="Track",
                    style="Track", s=200,
                    palette={"A: Collapse": "#ff2a6d", "B: Strategic": "#05d9e8"})

    plt.title("Narrative Agency Analysis", fontsize=16, weight='bold')
    plt.xlabel("Shannon Entropy")
    plt.ylabel("Agency Index")

    output_path = ensure_output_dir(config) / "story_analysis.png"
    plt.savefig(output_path, dpi=300)
    plt.close()

    print(f"✓ Saved: {output_path}")


def run_build_dataset(config):
    """
    Build a CSV dataset from all story files.
    Uses HTML sanitization to extract narrative content, stripping CSS/JS.
    This can be uploaded to HuggingFace or used for ML training.
    """
    print("\n" + "="*50)
    print("RUNNING: Build Dataset (with HTML Sanitization)")
    print("="*50)

    import glob
    import pandas as pd
    from build_dataset import clean_html_content

    data = []

    # Track A
    track_a_path = config['stories']['track_a']
    for f in glob.glob(f"{track_a_path}/*.html"):
        with open(f, encoding='utf-8') as file:
            raw_html = file.read()
            clean_text = clean_html_content(raw_html)
            if len(clean_text) > 50:  # Filter empty/navigation-only files
                data.append({
                    "text": clean_text,
                    "label": 0,
                    "label_name": "recursive_mode_collapse",
                    "track": "A",
                    "file_name": Path(f).name
                })

    # Track B
    track_b_path = config['stories']['track_b']
    for f in glob.glob(f"{track_b_path}/*.html"):
        with open(f, encoding='utf-8') as file:
            raw_html = file.read()
            clean_text = clean_html_content(raw_html)
            if len(clean_text) > 50:
                data.append({
                    "text": clean_text,
                    "label": 1,
                    "label_name": "strategic_agency",
                    "track": "B",
                    "file_name": Path(f).name
                })

    if not data:
        print("WARNING: No story files found! Check paths in config.yaml")
        return

    df = pd.DataFrame(data).sort_values(['track', 'file_name'])

    output_path = config['output']['dataset_file']
    df.to_csv(output_path, index=False)

    print(f"Valid data points: {len(df)}")
    print(f"Track A: {len([d for d in data if d['track'] == 'A'])}")
    print(f"Track B: {len([d for d in data if d['track'] == 'B'])}")

    # Preview sample to verify sanitization
    if len(df) > 0:
        sample = df.iloc[0]['text'][:100]
        print(f"Sample text: {sample}...")

    print(f"✓ Saved: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Narrative Analysis Pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run_pipeline.py --all           Run everything
  python run_pipeline.py --simulation    Just the heatmap simulation
  python run_pipeline.py --analyze       Just analyze story files
  python run_pipeline.py --dataset       Just build the CSV
        """
    )

    parser.add_argument('--all', action='store_true',
                        help='Run all analyses')
    parser.add_argument('--simulation', action='store_true',
                        help='Run agent simulation (generates heatmap)')
    parser.add_argument('--analyze', action='store_true',
                        help='Analyze story files')
    parser.add_argument('--dataset', action='store_true',
                        help='Build CSV dataset')

    args = parser.parse_args()

    # If no arguments, show help
    if not any([args.all, args.simulation, args.analyze, args.dataset]):
        parser.print_help()
        return

    config = load_config()

    print("\n" + "="*50)
    print("NARRATIVE ANALYSIS PIPELINE")
    print("="*50)
    print(f"Config loaded from: config.yaml")

    if args.all or args.simulation:
        run_simulation(config)

    if args.all or args.analyze:
        run_story_analysis(config)

    if args.all or args.dataset:
        run_build_dataset(config)

    print("\n" + "="*50)
    print("PIPELINE COMPLETE")
    print("="*50)


if __name__ == "__main__":
    main()
