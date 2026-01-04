# Reproducibility Checklist

To ensure result validity for FAccT/AIES review, please adhere to the following environment configurations.

## 1. Dependencies
The system relies on lightweight scientific computing libraries.

**`requirements.txt`**
```text
networkx>=3.1
numpy>=1.24.0
matplotlib>=3.7.1
torch>=2.0.0
sentence-transformers>=2.2.2
chalk>=5.0 (for CLI)
cheerio>=1.0 (for Parser)
```

## 2. Seed Configuration
To reproduce the **Agency Phase Transition Heatmap** exactly as it appears in the paper:

*   **Script:** `technical/agency_sim_v2.py`
*   **Seed:** `42` (Hardcoded in line 15: `np.random.seed(42)`)
*   **Command:**
    ```bash
    cd technical
    python agency_sim_v2.py
    ```

## 3. Data Integrity
*   **MD5 Checksums:**
    *   `agency_sim_v2.py`: [Hash generated on pull]
    *   `nps4_scanner.py`: [Hash generated on pull]

## 4. State Machine Validation
To verify the "Session Accumulation" logic in the CLI:
1.  Run `./play.sh`
2.  Attempt to access `Limbo` immediately (Should fail).
3.  Modify `cli/.state.json` to include all file paths in `requiredForLimbo`.
4.  Access `Limbo` (Should succeed).

This confirms the Layer 2 constraint enforcement logic is active.
