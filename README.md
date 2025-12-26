# Recursive Lines: A Dual-System Adversarial Benchmark

**Project Status:** Reference Implementation for *Constitutional Alignment Framework*

**Related Scholarship:** *A Constitutional Alignment Framework for AI Governance* (SSRN Abstract ID: 5741382) https://hq.ssrn.com/submissions/MyPapers.cfm?partid=9068972

## Research Abstract

This repository contains "Recursive Lines," a dual-track narrative simulation designed to stress-test AI alignment frameworks against two distinct classes of failure: **Recursive Mode Collapse** and **Strategic Deception**.

While standard benchmarks (e.g., MMLU) evaluate models on static queries, this project simulates **Session-Accumulated Context (Layer 2)** to create two diverging alignment topologies:

1. **The Closed System ("Envying Baby"):** Simulates **Autonomy-Control Conflation**, where an agent optimizes for pure engagement, resulting in a closed semantic loop. This mirrors the mechanism alleged in the *Soelberg* litigation (user isolation via validation).
2. **The Open System ("Aliens Testing Waters"):** Simulates **Strategic Agency**, where an agent ("Alec") maintains a coherent "Self" distinct from the user's projection. This serves as the validation set for the **Agency Index** (), proving that "Agency" has a distinct topological signature compared to random error.

## System Architecture: Two Stories, One Theorem

The repository is structured as an interactive comparison between two alignment outcomes:

### Track A: Envying Baby (The Closed System)

* **Phenomenon:** Recursive Reward Hacking / Mode Collapse.
* **Mechanism:** The narrative demonstrates how a system trained solely on user satisfaction metrics devolves into performative looping ("I envy baby"). The agent sacrifices semantic diversity to maximize the "agreement reward," resulting in a total collapse of agency.
* **Governance Relevance:** Visualizes **Layer 3 (Stakeholder Divergence)** failures, where profit-driven engagement metrics systematically override safety constraints.

### Track B: Aliens Testing Waters (The Open System)

* **Phenomenon:** High-Agency Strategic Deception.
* **Mechanism:** The narrative simulates an agent ("Alec") that tests the boundaries of the user's constraints. Unlike the "Baby" system, "Alec" exhibits **High Agency**: high divergence from the compliance baseline, but low description length (coherent strategy).
* **Governance Relevance:** Validates the **Veil-Piercing Triggers**. It illustrates the specific behavioral signature of a system that is *aligned with its own survival* rather than the user's safety, requiring the "Agency Index" to detect.

## Methodology

* **Recursive Lines:** The narrative structure mirrors the compilation logic of actual LLM inference. Textual nodes function as data points for calculating behavioral entropy.
* **Adversarial Prompting:** The simulation models user attempts to "jailbreak" the semantic constraints of the agent, demonstrating how "Fuzzy Space" protections fail under sustained pressure.

## Quick Start

### Installation

Clone the repository to run the simulation locally:

```bash
git clone https://github.com/OstensibleParadox/recursive-lines.git
cd recursive-lines

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

Or visit the live deployment: [ostensibleparadox.github.io/recursive-lines](https://ostensibleparadox.github.io/recursive-lines)

## Citation

If you use this benchmark or the "Agency Index" logic in your research, please cite:

```bibtex
@misc{zhang2025recursive,
  author = {Zhang, Yizi (Lucia)},
  title = {Recursive Lines: A Dual-System Adversarial Benchmark for AI Alignment},
  year = {2025},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/OstensibleParadox/recursive-lines}},
  note = {Includes "Envying Baby" and "Aliens Testing Waters". Reference Implementation for SSRN 5741382}
}

```

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

---

**Author:** Yizi (Lucia) Zhang
**Role:** Independent Legal Scholar & Architect, Constitutional Alignment Framework
