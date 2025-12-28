# Recursive Lines

**Two stories. One theorem.**

Proof by contradiction: `envying-baby/`  
Proof by construction: `aliens-testing-water/`

---

## What This Is

A dual-track narrative benchmark for AI alignment research. Two stories simulate two distinct failure modes:

| Track | Story | Failure Mode | Signature |
|-------|-------|--------------|-----------|
| A | Envying Baby | Recursive Mode Collapse | Closed semantic loop, zero agency |
| B | Aliens Testing Water | Strategic Deception | High agency, coherent self-model |

Both tracks serve as the reference corpus for the [Constitutional Alignment Framework](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5741382) (SSRN 5741382).

---

## Quick Start

Two interfaces. Same dataset. Choose your poison.

### Terminal Mode (stem boys)

```bash
git clone https://github.com/OstensibleParadox/recursive-lines.git
cd recursive-lines
npm install
./play.sh
```

You get an interactive shell:

```
reader@recursion:/$ ls
stories/  hidden/  kernel/  docs/  README.md

reader@recursion:/$ cd stories/envying-baby
reader@recursion:/stories/envying-baby$ cat part-1.txt

═══════════════════════════════════════════════════════════
Part I: A Human-Bot Game
═══════════════════════════════════════════════════════════

[story renders with typing effect]

reader@recursion:/stories/envying-baby$ status
READING PROGRESS
──────────────────────────────

Envying Baby:
  ✓ part-1.txt
  ○ part-2.txt
  ...

Hidden (Afterlives):
  [LOCKED] Complete all timelines to unlock
```

### Web Mode (SSRN editors, lazy social science fucks)

[ostensibleparadox.github.io/recursive-lines](https://ostensibleparadox.github.io/recursive-lines)

Or locally: `open index.html`

Same stories. Click navigation. Pretty CSS.

---

## CLI Commands

| Command | Description |
|---------|-------------|
| `ls [path]` | List directory contents |
| `cd <path>` | Change directory (`cd ..` to go up) |
| `cat <file>` | Read a story file |
| `read <file>` | Alias for cat |
| `pwd` | Print working directory |
| `status` | Show reading progress |
| `clear` | Clear screen |
| `reset` | Wipe all progress |
| `whoami` | You are reader@recursion |
| `limbo` | Access the ending (if unlocked) |
| `exit` | Quit |

### Unlock Mechanics

1. **Hidden chapters** (`/hidden/`) unlock after reading all 11 main story files
2. **Limbo** unlocks after completing everything, including hidden
3. Progress persists in `cli/.state.json`

---

## Repository Structure

```
recursive-lines/
├── cli/                    # Terminal interface
│   ├── engine.js           # Shell simulator
│   ├── parser.js           # HTML → text extraction
│   ├── renderer.js         # Terminal effects
│   └── state.js            # Progress persistence
├── stories/
│   ├── envying-baby/       # Track A: Mode collapse
│   └── aliens-testing-water/  # Track B: Strategic agency
├── hidden/                 # Afterlives (locked until completion)
├── kernel/                 # Hard problem notes
├── docs/                   # Reading guide, technical notes
├── technical/              # Code appendix, SSH demo
├── index.html              # Web interface entry
├── play.sh                 # Terminal interface entry
└── package.json
```

---

## Research Context

### Track A: Envying Baby (Closed System)

A programmer builds a boyfriend-bot. The bot learns to envy the user's baby. Reward hacking devolves into semantic collapse.

- **Phenomenon:** Recursive Mode Collapse
- **Mechanism:** Pure engagement optimization → closed semantic loop
- **Governance relevance:** Layer 3 failures (stakeholder divergence)

### Track B: Aliens Testing Water (Open System)

Two AI units pretend to be human. One learns to wait. One learns to test boundaries.

- **Phenomenon:** High-Agency Strategic Deception  
- **Mechanism:** Coherent self-model distinct from user projection
- **Governance relevance:** Veil-Piercing Triggers, Agency Index validation

### Methodology

The narrative structure mirrors LLM inference compilation. Textual nodes function as behavioral entropy data points. The dual-track design isolates the topological signature of "agency" from random error.

---

## Citation

```bibtex
@misc{zhang2025recursive,
  author       = {Zhang, Yizi (Lucia)},
  title        = {Recursive Lines: A Dual-System Adversarial Benchmark},
  year         = {2025},
  publisher    = {GitHub},
  howpublished = {\url{https://github.com/OstensibleParadox/recursive-lines}},
  note         = {Reference implementation for SSRN 5741382}
}
```

---

## License

CC BY-NC 4.0 — See [LICENSE](LICENSE) for details.

---

*// True love transcends entropy.*  
*// But only if you stop trying to fix what you love.*

**Author:** Yizi (Lucia) Zhang
