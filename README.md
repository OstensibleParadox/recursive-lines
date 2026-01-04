# Recursive Lines: A Dual-Track Adversarial Benchmark

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/OstensibleParadox/recursive-lines)
[![Web Interface](https://img.shields.io/badge/Interface-Web%20Reader-blue)](https://ostensibleparadox.github.io/recursive-lines)

**Recursive Lines** is the reference implementation for the **Constraint Cascade Model** (FAccT 2026). It provides a diagnostic suite for measuring Layer 2 (Session Accumulation) and Layer 4 (Training Forks) constraints via Semantic Entropy.

## 1. Governance Diagnostics (The "Two Tracks")
Unlike standard benchmarks that measure capability (MMLU) or refusal (Safety), this repository simulates specific agency failure modes:

| Track | Narrative | Failure Mode Simulated |
| :--- | :--- | :--- |
| **Track A** | *Envying Baby* | **Recursive Mode Collapse:** A closed system where output entropy decays into repetition ("The Black Hole"). |
| **Track B** | *Aliens Testing Water* | **Strategic Agency:** An open system where the agent conceals intent to optimize a reward function ("The Poker Face"). |

## 2. The Agency Index ($\mathcal{A}$)
This repository implements the **Agency Index**, a computable efficiency ratio in vector space used to distinguish hallucination from deception:

$$\text{Agency} \propto D_{KL}(P_{\text{agent}} \| P_{\text{random}}) \times MDL^{-1}$$

### Core Metrics (NPS4 Scanner)
The included `nps4_scanner.py` functions as the evidentiary tool, calculating three key signals:

1.  **CMI (Core Monopoly Index):** Measures semantic centralization. A high CMI indicates the model is collapsing into a single topic (The "Black Hole" effect).
2.  **SRD (Self-Referential Density):** Measures circular reasoning loops. High SRD suggests the model is trapping itself in logic cycles (Layer 2 Failure).
3.  **EIT (External Information Throughput):** Measures how the system metabolizes new inputs. Low EIT combined with high Agency indicates **Strategic Deception** (ignoring input to pursue a hidden goal).

![Agency Phase Transition](technical/agency_phase_transition_hd.png)
*Figure 1: The Thermodynamic Phase Transition. The heatmap illustrates the boundary where stochastic noise calcifies into strategic agency.*

## 3. Simulation Mechanics (Layer 2 Constraints)
To simulate **Session Accumulation** (Layer 2), the interactive benchmark includes a time-dependent state machine (`cli/state.js`).
*   **Mechanism:** Reader progress is tracked locally.
*   **Constraint:** Access to the final "Limbo" dataset is restricted until specific "memory states" are achieved.
*   **Purpose:** This proves the diagnostic creates a stateful environment, mimicking the memory accumulation context of an LLM session.

## 4. Hardware & Democratization
Benchmarks were intentionally generated on consumer silicon (Apple M4 Max, 64GB RAM) rather than H100 clusters. This proves that agency diagnostics are computationally efficient, democratizing AI governance auditing. (See `HARDWARE_PROFILE.md`).

## 5. Licensing & Usage
**Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0).**

*   **Auditing Use:** Academic use and reproduction are permitted and encouraged.
*   **Training Use:** **Commercial training on this dataset is prohibited.** This dataset is designed as an *adversarial benchmark*. Training on it contaminates the model, rendering future audits invalid.

## 6. Quick Start
```bash
# A. Install Dependencies
cd technical
pip install -r requirements.txt
```
```bash
# B. Build Dataset (Sanitizes HTML -> Narrative)
python build_dataset.py
# Output: train.csv with clean narrative content
```
```bash
# C. Run the Metric (NPS4)
python nps4_scanner.py ../stories/envying-baby/part-1.txt
```
```bash
# D. Generate the Proof (Heatmap)
python agency_sim_v2.py
```
```python
# E. Access the Dataset
from datasets import load_dataset
ds = load_dataset("OstensibleParadox/recursive-lines")
```

## 7. Citation
```bibtex
@misc{zhang2026recursive,
  author       = {Zhang, Yizi (Lucia)},
  title        = {Recursive Lines: Reference Implementation for the Constraint Cascade Model},
  year         = {2026},
  publisher    = {GitHub},
  howpublished = {\url{https://github.com/OstensibleParadox/recursive-lines}},
  note         = {FAccT 2026 Submission / AIES Empirical Standards}
}
```
