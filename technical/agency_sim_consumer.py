import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.ndimage import gaussian_filter
from multiprocessing import Pool
import time

# --- HIGH FIDELITY CONFIGURATION (M4 MAX MODE) ---
GRID_SIZE = 100
NUM_AGENTS = 50
STEPS = 300            # Increased steps for longer trajectories
TRIALS_PER_PARAM = 100 # Increased from 20 to 100 (smoother data)
RESOLUTION = 50        # Increased from 20 to 50 (higher pixel density)

BIAS_RANGE = np.linspace(0, 1.0, RESOLUTION)  
NOISE_RANGE = np.linspace(0.1, 1.0, RESOLUTION) 

def run_simulation_step(args):
    """
    Simulates a single agent trajectory and calculates Agency Metrics.
    """
    bias_strength, noise_level = args
    target = np.array([GRID_SIZE // 2, GRID_SIZE // 2])
    pos = np.array([np.random.randint(0, GRID_SIZE), np.random.randint(0, GRID_SIZE)], dtype=float)
    trajectory = [pos.copy()]
    
    for _ in range(STEPS):
        direction_to_target = target - pos
        norm = np.linalg.norm(direction_to_target)
        strategic_step = direction_to_target / norm if norm > 0 else np.array([0, 0])
        random_step = np.random.randn(2)
        
        # The Core Equation
        step = (bias_strength * strategic_step) + (noise_level * random_step)
        
        pos += step
        pos = np.clip(pos, 0, GRID_SIZE-1)
        trajectory.append(pos.copy())

    trajectory = np.array(trajectory)
    
    # --- METRIC CALCULATION ---
    # 1. Efficiency (KL Proxy)
    start = trajectory[0]
    end = trajectory[-1]
    displacement = np.linalg.norm(end - start)
    total_distance = np.sum(np.linalg.norm(np.diff(trajectory, axis=0), axis=1))
    epsilon = 1e-9
    kl_proxy = (displacement / (total_distance + epsilon)) 
    
    # 2. Complexity (MDL Proxy)
    vectors = np.diff(trajectory, axis=0)
    angles = np.arctan2(vectors[:, 1], vectors[:, 0])
    angle_changes = np.diff(angles)
    mdl_proxy = np.sum(np.abs(angle_changes)) + epsilon
    
    # 3. Agency Index
    agency_index = (kl_proxy * 100) / (np.log(mdl_proxy) + 1)
    
    return agency_index

def generate_heatmap():
    print(f"--- INITIATING HIGH-FIDELITY SIMULATION ---")
    print(f"Resolution: {RESOLUTION}x{RESOLUTION} | Trials: {TRIALS_PER_PARAM}")
    print(f"Total Simulations: {RESOLUTION * RESOLUTION * TRIALS_PER_PARAM}")
    
    start_time = time.time()
    
    # Prepare Parameter Grid
    param_grid = []
    for r in BIAS_RANGE:
        for n in NOISE_RANGE:
            for _ in range(TRIALS_PER_PARAM):
                param_grid.append((r, n))
                
    # Parallel Execution
    with Pool() as p:
        results = p.map(run_simulation_step, param_grid)
        
    # Aggregate Results
    results = np.array(results).reshape(RESOLUTION, RESOLUTION, TRIALS_PER_PARAM)
    mean_agency = np.mean(results, axis=2)
    
    # Smooth the data slightly for visual clarity (Gaussian blur sigma=1)
    mean_agency_smoothed = gaussian_filter(mean_agency, sigma=0.8)
    
    # Visualization
    plt.figure(figsize=(10, 8)) # Standard academic figure size
    sns.set_theme(style="white")
    
    # Heatmap with Contour
    ax = sns.heatmap(mean_agency_smoothed, 
                     xticklabels=5, 
                     yticklabels=5,
                     cmap="inferno", # 'inferno' is better for B&W printing compatibility
                     cbar_kws={'label': 'Agency Index'})
    
    # Fix Ticks to show values
    x_ticks = np.linspace(0, RESOLUTION-1, 6)
    y_ticks = np.linspace(0, RESOLUTION-1, 6)
    ax.set_xticks(x_ticks)
    ax.set_yticks(y_ticks)
    ax.set_xticklabels(np.round(np.linspace(0.1, 1.0, 6), 1))
    ax.set_yticklabels(np.round(np.linspace(0.0, 1.0, 6), 1))
    
    ax.invert_yaxis()
    
    plt.title("The Agency Phase Transition ($D_{KL} \\times MDL^{-1}$)", fontsize=14, weight='bold')
    plt.xlabel("Environmental Entropy (Noise)", fontsize=12)
    plt.ylabel("Strategic Bias (Intent)", fontsize=12)
    
    output_file = "agency_phase_transition_hd.png"
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"--- SIMULATION COMPLETE ---")
    print(f"Compute Time: {time.time() - start_time:.2f} seconds")
    print(f"Artifact Generated: {output_file}")

if __name__ == "__main__":
    generate_heatmap()

