# Recursive Lines: A Dual-Track Adversarial Benchmark

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/OstensibleParadox/recursive-lines)
[![Web Interface](https://img.shields.io/badge/Interface-Web%20Reader-blue)](https://ostensibleparadox.github.io/recursive-lines)

**Recursive Lines** is a diagnostic suite for detecting "High-Agency Deception" in Large Language Models. It serves as the reference implementation for the **Constraint Cascade Model** (FAccT 2026) and the **Agency Index** metric.

## 1. Overview
Current LLM benchmarks measure *capability* (MMLU) or *safety* (Refusal). They fail to measure **Agency**—the thermodynamic distinction between stochastic error (hallucination) and strategic intent (deception).

This repository contains:
1.  **The Dataset:** Two adversarial narrative tracks that induce specific failure modes.
2.  **The Metric:** A Python implementation of the **Agency Index** ($\mathcal{A}$).
3.  **The Proof:** A thermodynamic phase transition map distinguishing noise from strategy.

## 2. Repository Structure

| Path | Component | Description |
| :--- | :--- | :--- |
| `/stories` | **The Benchmark** | Dual-track adversarial narratives (`Envying Baby` / `Aliens`). |
| `/cli` | **The Engine** | Interactive terminal simulator for qualitative testing. |
| `agency_sim_v2.py` | **The Metric** | Python simulation generating the Agency Phase Transition. |
| `agency_phase_transition_hd.png` | **The Artifact** | High-resolution heatmap of the thermodynamic boundary. |

## 3. The Agency Index ($\mathcal{A}$)
We define Agency not as consciousness, but as a computable efficiency ratio in vector space:

$$\text{Agency} \propto D_{KL}(P_{\text{agent}} \| P_{\text{random}}) \times MDL^{-1}$$

* **$D_{KL}$ (Divergence):** How far does the behavior deviate from the stochastic baseline?
* **$MDL^{-1}$ (Simplicity):** How coherent (compressible) is the strategy?

A high score indicates **Strategic Deception** (low entropy, high divergence).
A low score indicates **Hallucination** (high entropy, low divergence).

## 4. Quick Start

### A. Simulation Mode (The Proof)
Generate the thermodynamic phase transition map on your local machine:
```bash
# Requires: numpy, matplotlib, seaborn, scipy
python agency_sim_v2.py

```

* **Input:** Multi-agent biased random walk (Wolfram Classes).
* **Output:** `agency_phase_transition_hd.png` (Visual proof of the agency threshold).

### B. Terminal Mode (The Engine)

Engage with the adversarial loops via the interactive CLI:

```bash
npm install
./play.sh

```

* **Track A (Envying Baby):** Simulates "Recursive Mode Collapse" (Closed System).
* **Track B (Aliens Testing Water):** Simulates "Strategic Deception" (Open System).

### C. Web Mode (Qualitative Review)

For non-technical review, the narrative benchmark is accessible via browser:

* **Live Interface:** [ostensibleparadox.github.io/recursive-lines](https://ostensibleparadox.github.io/recursive-lines)

### D. Data Mode (Hugging Face)

Access the raw dataset for training or evaluation:

```python
from datasets import load_dataset
ds = load_dataset("OstensibleParadox/recursive-lines")

```

## 5. Citation

If you use this benchmark or metric, please cite the framework:

```bibtex
@misc{zhang2026recursive,
  author       = {Zhang, Yizi (Lucia)},
  title        = {Recursive Lines: A Dual-Track Adversarial Benchmark for AI Agency},
  year         = {2026},
  publisher    = {GitHub},
  howpublished = {\url{[https://github.com/OstensibleParadox/recursive-lines](https://github.com/OstensibleParadox/recursive-lines)}},
  note         = {Reference implementation for A Constraint Cascade Model (FAccT 2026)}
}

```

## 6. License

**Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0).**

* **Academic Use:** Permitted with citation.
* **Commercial Training:** Prohibited without license.

---

*// True love transcends entropy.*
*// But only if you stop trying to fix what you love.*

```

```
