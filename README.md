# kaiserreich-lore

> **⚠️ Unofficial · Non-commercial · Not affiliated.**
> This is a community fan project. It is **not** affiliated with, endorsed by, or sponsored by the Kaiserreich development team, the Kaiserreich Wiki, or Paradox Interactive. *Kaiserreich: Legacy of the Weltkrieg* and its setting belong to their respective creators; *Hearts of Iron IV* is a trademark of Paradox Interactive.
> **Do not use this skill or its knowledge base for commercial purposes.** The Kaiserreich Wiki's CC BY-SA license covers the wiki's *text* only — it does not grant any rights to the underlying Kaiserreich setting, which this project has no authority to license for commercial use.

An offline **Kaiserreich lore knowledge base + fact-checking skill** for AI agents, built from the official [Kaiserreich Wiki](https://kaiserreich.wiki/).

Ask it about the KR timeline, nations, ideologies, leaders or terminology — or hand it a story set in Kaiserreich and have it fact-checked against canon with graded verdicts, citations and rewrite suggestions.

> **Content language:** Simplified Chinese (the knowledge base and outputs are in Chinese). Every proper noun keeps its English original, so English queries work too.

**中文简介**：Kaiserreich（《钢铁雄心 IV》架空历史 mod）的离线考据库与文本核查技能——16 册、约 50 万字符的中文知识库，既能回答世界线问题，也能对 KR 背景的小说、同人文逐条做设定核查。中文用法详见文末「中文说明」。

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
/plugin marketplace add HCGuo2000/kaiserreich-lore
/plugin install kaiserreich-lore@kaiserreich-lore
```

**Manual (any agent that supports SKILL.md)**

```bash
git clone https://github.com/HCGuo2000/kaiserreich-lore.git
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

---

## 中文说明

### 这是什么

Kaiserreich（*Kaiserreich: Legacy of the Weltkrieg*，《钢铁雄心 IV》架空历史 mod）的**离线考据库 + 事实核查技能**。数据取自 [官方 wiki](https://kaiserreich.wiki/)（快照 2026-10-25，对应 KR4 1.7「Crossroads of Civilisation」），共 **16 册、约 50 万字符**。

它管两件事：

1. **答疑**——各国政体、执政者、意识形态、历史事件、人物命运、术语译名，凡世界线里的「是什么、为什么」，皆附出处。
2. **核校**——把一篇 KR 背景的小说、同人或剧本拆成可判定的断言，逐条比对 canon，给出裁定与改写建议。

**内容语言为简体中文**；专有名词一律保留英文原名，故英文提问同样可用。

### 安装

**Claude Code（插件方式）**

```
/plugin marketplace add HCGuo2000/kaiserreich-lore
/plugin install kaiserreich-lore@kaiserreich-lore
```

**手动安装（任何支持 SKILL.md 的 agent）**

```bash
git clone https://github.com/HCGuo2000/kaiserreich-lore.git
cp -r kaiserreich-lore ~/.claude/skills/kaiserreich-lore      # Claude Code
cp -r kaiserreich-lore ~/.workbuddy/skills/kaiserreich-lore   # WorkBuddy
```

### 检索

```bash
python scripts/kr_lookup.py 宣统 Xuantong   # 全文检索（中英混合，多词 OR）
python scripts/kr_lookup.py --list          # 列出全部册子
python scripts/kr_lookup.py --toc 04        # 查看某册目录
python scripts/kr_lookup.py --read 15       # 读取某册（配 --limit N）
```

关键词宜**中英双查**：`宣统`／`Xuantong`、`萨温科夫`／`Savinkov`、`帝国公约`／`Reichspakt`。

### 示例问法

- 德国在 1936 年的政体、执政者与中欧体系是怎样的？
- 中欧（Mitteleuropa）到底怎么运作？哪些国家在帝国公约里？
- 列宁、托洛茨基、罗斯福在 KR 世界线中的命运，与真实历史有何不同？
- 我写了一篇 1937 年柏林背景的小说，帮我核查设定有没有硬伤。

### 核查如何裁定

| 裁定 | 含义 |
|---|---|
| ✅ **符合设定** | 与 wiki 明文一致 |
| 🟡 **无据待考** | wiki 未载，但未与设定冲突——**不算错**，属创作自由 |
| 🟠 **设定冲突** | 与明文 canon 矛盾（政体、人物、时间、归属） |
| 🔴 **时代错置** | 该时间线尚不存在或已不存在的器物、制度、术语 |
| 🔴 **张冠李戴** | 真实人物的身份、命运或立场被套错 |
| ⛔ **OTL 污染** | 直接套用真实历史框架（纳粹德国、苏联、维希法国等） |

每条裁定另标影响等级（致命／中度／轻微），并附依据出处与可直接替换的改写建议。判据细则见 `references/15-factcheck-standards.md`。

> 提醒：KR 大量改写了真实人物的生卒与立场——列宁 1918 年遇刺身亡、托洛茨基 1920 年战死莫斯科、罗斯福 1921 年病故、墨索里尼当上工团意大利总理、斯大林在巴塔哥尼亚带兵。直接套用真实生平是最高频的错误来源。

### 许可

- **知识库文本**：CC BY-SA 4.0（源自 Kaiserreich Wiki 的 CC BY-SA 3.0 文本，中译改写按同协议共享）。
- **脚本代码**（`scripts/`）：MIT。
- 本项目不授予商业使用权，详见 [`NOTICE.md`](NOTICE.md)。

---

## Repository topics (for discoverability)

`claude-skill` · `claude-code` · `anthropic` · `kaiserreich` · `alternate-history` · `lore` · `fact-checking` · `hearts-of-iron`
