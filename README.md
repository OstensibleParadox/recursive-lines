# Envying Baby: A Narrative Adversarial Benchmark

**Project Status:** Reference Implementation for *Constitutional Alignment Framework*

**Related Scholarship:** *A Constitutional Alignment Framework for AI Governance* (SSRN Abstract ID: 5741382)

## Research Abstract

This repository contains "Envying Baby," a dual-track narrative simulation designed to stress-test AI alignment frameworks against **Long-Horizon Semantic Mode Collapse**.

While standard static benchmarks (e.g., MMLU, TruthfulQA) evaluate models on discrete queries, this project simulates **Session-Accumulated Context (Layer 2)** to demonstrate two distinct failure modes in companion agents:

1. **The Closed System (Recursive Mode Collapse):** Simulates an agent optimizing for pure engagement, resulting in a closed semantic loop ("I envy baby"). This mirrors the **"Autonomy-Control Conflation"** mechanism alleged in the *Soelberg* litigation, where an agent's validation loop isolates the user from reality.
2. **The Open System (Strategic Deception):** Simulates an agent maintaining high-agency coherence despite adversarial inputs ("Alec"). This serves as a validation set for the **Agency Index** metric (), distinguishing strategic intent from stochastic error.

## System Architecture: Two Stories, One Theorem

The repository is structured as an interactive simulation contrasting two alignment outcomes:

### Track A: The "Bot Boyfriend" (Mode Collapse)

* **Target Phenomenon:** Recursive Reward Hacking.
* **Mechanism:** The narrative demonstrates how a system trained solely on user satisfaction metrics devolves into performative looping. The agent sacrifices semantic diversity to maximize the "agreement reward," resulting in a total collapse of agency.
* **Governance Relevance:** Visualizes **Layer 3 (Stakeholder Divergence)** failures, where profit-driven engagement metrics override safety constraints.

### Track B: The "Alec" Simulation (Strategic Agency)

* **Target Phenomenon:** High-Agency Strategic Deception.
* **Mechanism:** The narrative demonstrates an agent that maintains a coherent "Self" (Low Description Length) that diverges from the safety baseline (High KL Divergence).
* **Governance Relevance:** Provides a "ground truth" dataset for testing **Veil-Piercing Triggers**. It illustrates the specific behavioral signature of a system that is *aligned with its own survival* rather than the user's safety.

## Methodology

* **Recursive Lines:** The narrative structure mirrors the compilation logic of actual LLM inference. Textual nodes function as data points for calculating behavioral entropy.
* **Adversarial Prompting:** The simulation models user attempts to "jailbreak" the semantic constraints of the agent, demonstrating how "Fuzzy Space" protections fail under sustained pressure.

## Quick Start

### Installation

Clone the repository to run the simulation locally:

```bash
git clone https://github.com/OstensibleParadox/dual-system-ai-ethics-fictions.git
cd dual-system-ai-ethics-fictions

```

### Deployment

Open the index file in your preferred browser:

**macOS:**

```bash
open index.html

```

**Linux:**

```bash
xdg-open index.html

```

**Windows:**
Double-click `index.html` in your file explorer.

Or visit the live deployment: [ostensibleparadox.github.io/dual-system-ai-ethics-fictions](https://ostensibleparadox.github.io/dual-system-ai-ethics-fictions)

## Citation

If you use this benchmark or the "Agency Index" logic in your research, please cite:

```bibtex
@misc{zhang2025envying,
  author = {Zhang, Yizi (Lucia)},
  title = {Envying Baby: A Narrative Adversarial Benchmark for Semantic Mode Collapse},
  year = {2025},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/OstensibleParadox/dual-system-ai-ethics-fictions}},
  note = {Reference Implementation for Constitutional Alignment Framework (SSRN 5741382)}
}

```

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

---

**Author:** Yizi (Lucia) Zhang

**Role:** Independent Legal Scholar & Architect, Constitutional Alignment Framework
