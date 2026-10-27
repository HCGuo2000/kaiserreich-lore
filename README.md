# kaiserreich-lore

An offline **Kaiserreich lore knowledge base + fact-checking skill** for AI agents, built from the official [Kaiserreich Wiki](https://kaiserreich.wiki/).

Ask it about the KR timeline, nations, ideologies, leaders or terminology — or hand it a story set in Kaiserreich and have it fact-checked against canon with graded verdicts, citations and rewrite suggestions.

> **Content language:** Simplified Chinese (the knowledge base and outputs are in Chinese). Every proper noun keeps its English original, so English queries work too.

---

## What's inside

16 volumes, ~500k characters, collected on **2026-10-25** from the official wiki; aligned to **KR4 1.7 "Crossroads of Civilisation" (2026-09-18)**.

| Vol | File | Contents |
|---|---|---|
| 00 | `references/00-index.md` | Core-facts card, routing table, retrieval method, known gaps |
| 01 | `references/01-podt.md` | The Weltkrieg, armistices and treaties, postwar order, Russian Civil War, French/British revolutions, divergence list vs OTL |
| 02 | `references/02-timeline.md` | Year-by-year timeline, 1919–1935 |
| 03 | `references/03-ideologies.md` | The ten ideologies in depth |
| 04 | `references/04-germany-mitteleuropa.md` | Germany, Mitteleuropa, Reichspakt, eastern client states |
| 05 | `references/05-internationale.md` | Third International, Commune of France, Union of Britain, SRI |
| 06 | `references/06-entente.md` | Entente, Canada, French Republic in exile, Sardinia, Australasia, India |
| 07 | `references/07-russia-east.md` | Russia, Savinkov, Caucasus, Central Asia, Mongolia |
| 08 | `references/08-americas.md` | United States, Mexico, Brazil, Argentina, rest of the Americas |
| 09 | `references/09-asia.md` | China (Qing / Fengtian / warlords), Japan, Southeast Asia, South Asia |
| 10 | `references/10-africa-mideast.md` | Mittelafrika, Ottoman Empire, Persia, Egypt, North Africa |
| 11 | `references/11-key-events.md` | US 1936 constitutional crisis, Creditanstalt, Lake Lubahn, Xuantong Restoration, Yangtze Incident |
| 12 | `references/12-balkans-europe-minor.md` | Balkans, Spain, Papal States, Italian remnants |
| 13 | `references/13-people.md` | Heads of state and ruling parties by region |
| 14 | `references/14-glossary.md` | Terminology and translation conventions |
| 15 | `references/15-factcheck-standards.md` | **Verdict rules:** evidence tiers, six-grade verdicts, OTL-contamination list, character-fate reversal table, report template, in-wiki contradictions register |

## Retrieval script

Pure standard library, Python 3.8+.

```bash
python scripts/kr_lookup.py 宣统 Xuantong   # full-text search (mixed Chinese/English, OR)
python scripts/kr_lookup.py --list          # list volumes
python scripts/kr_lookup.py --toc 04        # show a volume's outline
python scripts/kr_lookup.py --read 15       # read a volume (with --limit N)
```

## Install

**Claude Code (as a plugin)**

```
/plugin marketplace add <your-github-owner>/kaiserreich-lore
/plugin install kaiserreich-lore@kaiserreich-lore
```

**Manual (any agent that supports SKILL.md)**

```bash
git clone https://github.com/<your-github-owner>/kaiserreich-lore.git
cp -r kaiserreich-lore ~/.claude/skills/kaiserreich-lore      # Claude Code
cp -r kaiserreich-lore ~/.workbuddy/skills/kaiserreich-lore   # WorkBuddy
```

## Example prompts

- What is Germany's political system and who leads it in 1936?
- How does Mitteleuropa actually work, and which states are in the Reichspakt?
- How do the fates of Lenin, Trotsky and Roosevelt differ from real history in this timeline?
- Here is a short story set in 1937 Berlin — fact-check it against Kaiserreich canon.

## How fact-checking works

Text is decomposed into atomic claims, each retrieved against the library and graded:

| Grade | Meaning |
|---|---|
| ✅ Canon-consistent | Matches the wiki |
| 🟡 Not attested | Not in the wiki, but not contradicted — **not an error** |
| 🟠 Contradiction | Conflicts with explicit canon |
| 🔴 Anachronism | Technology, institution or term that doesn't exist in this timeline |
| 🔴 Misattribution | A real person's fate or stance mapped wrongly |
| ⛔ OTL contamination | Real-history framework imposed (Nazi Germany, USSR, Vichy France…) |

Each verdict carries severity (fatal / moderate / minor), a citation, and a concrete rewrite suggestion.

## Known gaps

- Some wiki pages have no body text (e.g. `Second_American_Civil_War`, which has not happened as of the 1936 start date) — outcomes there are treated as **possibilities**, never as settled canon.
- A few Russian periphery states and two ideology subsections are empty or WIP on the source wiki.
- Game mechanics (focus trees, achievements, division templates) are out of scope: this is a lore library, not a strategy guide.
- Contradictions inside the source wiki are **registered and shown side by side** rather than silently reconciled (see `15` §7).

## License & attribution

- **Knowledge base text:** [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Derived from the [Kaiserreich Wiki](https://kaiserreich.wiki/), whose text is licensed CC BY-SA 3.0 — the Chinese translation and restructuring here is shared under the same terms.
- **Code (`scripts/`):** MIT.
- See [`NOTICE.md`](NOTICE.md) for full attribution.

This is an unofficial, non-commercial community project. It is not affiliated with the Kaiserreich development team or Paradox Interactive. *Kaiserreich* and its setting belong to their respective creators.

## Repository topics (for discoverability)

`claude-skill` · `claude-code` · `anthropic` · `kaiserreich` · `alternate-history` · `lore` · `fact-checking` · `hearts-of-iron`
