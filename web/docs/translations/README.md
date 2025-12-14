# Translations

Want to translate **Recursive Love** to another language? Here's how.

## Available Translations

Currently available:
- 🇺🇸 English (original)

In progress:
- 🇨🇳 Simplified Chinese (zh-CN)

Planned:
- 🇫🇷 French (fr)
- 🇩🇪 German (de)

## How to Contribute a Translation

### 1. Check if it's already in progress
Look in the `translations/` directory to see if someone is already working on your language.

### 2. Create a directory for your language
```bash
mkdir translations/[language-code]
# Example: mkdir translations/zh-CN
```

### 3. Translate the content
You'll need to translate:

**Core Stories:**
- `stories/envying-baby/index.html`
- `stories/envying-baby/special-timeline.html`
- `stories/envying-baby/general-timeline.html`
- `stories/aliens-testing-water/index.html`
- `stories/aliens-testing-water/phase-1.html` through `phase-5.html`

**Hidden Content:**
- `hidden/marriage-logs.html`
- `hidden/alec-final-thoughts.html`
- `hidden/blueprint.html`

**Documentation:**
- `README.md`
- `docs/about.md`
- `docs/technical-notes.md`
- `docs/reading-guide.md`

**Landing Page:**
- `index.html`

### 4. Translation Guidelines

**DO translate:**
- Story prose and dialogue
- Headers and navigation
- Documentation
- Console messages
- UI labels

**DON'T translate:**
- Code snippets (they're meant to be in English)
- Terminal commands (SSH, git, etc.)
- Technical terms that are universal (SSH, kernel, segfault, etc.)
- Variable names in code
- File paths

**CONSIDER carefully:**
- Character names (Alec and Ada are meaningful: A + 1 = B, Ada Lovelace)
- Technical metaphors (some might not translate well)
- Wordplay and puns
- Cultural references

### 5. Technical Adaptations

Some languages may need:
- Different fonts (update CSS)
- Right-to-left text support (Arabic, Hebrew)
- Different character encoding
- Adjusted line breaks and spacing

### 6. Submit Your Translation

1. Fork the repository
2. Create your translation in `translations/[language-code]/`
3. Test it thoroughly
4. Submit a pull request
5. Include a README in your language explaining any adaptation choices

## Translation Notes

### About the Code Metaphors

The core metaphor (code as emotional language) should work in most languages, but some nuances might be lost:

- **SSH** is universally understood by programmers
- **Git** terminology is usually used in English even in other languages
- **Unix commands** are standardized in English

Feel free to add footnotes or explanations where needed.

### About Character Names

**Alec** and **Ada** are:
- Short, pronounceable in most languages
- Sequential (A-lec, A-da → A, B)
- References to Alan Turing and Ada Lovelace (pioneers of computer science)

You can keep them in English or adapt them if there's a culturally appropriate equivalent that maintains the A/B pattern.

### About the Terminal Aesthetic

The green-on-black terminal look is culturally specific to Unix/Linux hacker culture. If your target language has different computing aesthetics, feel free to adapt the CSS, but try to maintain:

- Monospace font
- High contrast
- Retro/technical feel

## Language-Specific Directories

Each language should have:

```
translations/[language-code]/
├── README.md (in that language)
├── index.html (translated landing page)
├── stories/
│   ├── envying-baby/
│   └── aliens-testing-water/
├── hidden/
├── docs/
└── technical/ (optional - can link to English version)
```

## Questions?

Open an issue on GitHub or email the project maintainer.

Thank you for helping make this accessible to more people!

---

*Love transcends language barriers. Let's prove it.*
