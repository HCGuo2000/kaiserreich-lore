---
name: kaiserreich-lore
description: Kaiserreich (Hearts of Iron IV) alternate-history lore knowledge base and fact-checking skill. Use when answering questions about the KR timeline, nations, ideologies, leaders, events or terminology, or when fact-checking a story, fanfic or novel against Kaiserreich canon. Ships a 1919-1935 yearly timeline, ten ideologies, per-region nation dossiers, key crises, a character-fate reversal table and a six-grade verdict standard. Content language is Simplified Chinese; proper nouns keep their English originals.
version: 1.0.0
license: CC-BY-SA-4.0
---

# Kaiserreich 设定考据库 / Kaiserreich Lore Library

本 skill 提供一套**离线知识库 + 检索工具 + 核查裁判规则**，用于回答 Kaiserreich 世界观问题，以及对文学文本做设定事实核查。

An offline lore library plus a retrieval script and a fact-checking standard for *Kaiserreich: Legacy of the Weltkrieg*, the alternate-history mod for *Hearts of Iron IV*. The knowledge base is written in Simplified Chinese; every proper noun keeps its English original, so English queries work too.

- **数据源 / Source**：https://kaiserreich.wiki/ （官方 wiki，MediaWiki，2198 条目，in-universe 视角）
- **采集快照 / Snapshot**：2026-10-25
- **对应版本 / Game version**：KR4 1.7「Crossroads of Civilisation」（2026-09-18）
- **规模 / Size**：16 册，约 50 万字符
- **许可 / License**：CC BY-SA 4.0（源站为 CC BY-SA 3.0，见 §六）

---

## 一、知识库结构

路径：`references/`

| 册号 | 内容 |
|---|---|
| `00-index.md` | **入口必读**：世界观核心事实卡、分册路由表、检索方法、已知缺口 |
| `01-podt.md` | 世界大战、停战与和约、战后秩序、俄国内战、法英革命、与 OTL 分歧清单 |
| `02-timeline.md` | 1919–1935 逐年大事年表（按月，带领域标签） |
| `03-ideologies.md` | 十种意识形态详解 |
| `04-germany-mitteleuropa.md` | 德国、中欧与帝国公约、东方卫星国逐国简报 |
| `05-internationale.md` | 第三国际、法国公社、不列颠联盟、意大利社会主义共和国等 |
| `06-entente.md` | 协约国、加拿大、法兰西共和国（流亡）、撒丁、澳大拉西亚、印度 |
| `07-russia-east.md` | 俄国、萨温科夫、高加索、中亚、蒙古 |
| `08-americas.md` | 美国、墨西哥、巴西、阿根廷、南美与中美洲诸国 |
| `09-asia.md` | 中国（大清／奉天／军阀）、日本、东南亚、南亚 |
| `10-africa-mideast.md` | 中非殖民体系、奥斯曼、波斯、埃及、北非 |
| `11-key-events.md` | 美国 1936 宪政危机、信贷银行危机、卢班湖危机、宣统复辟、长江事件等 |
| `12-balkans-europe-minor.md` | 巴尔干诸国、西班牙、教宗国与意大利残余 |
| `13-people.md` | 各国元首与执政党总表、关键人物速查 |
| `14-glossary.md` | 术语与译名对照、译名规范 |
| `15-factcheck-standards.md` | **核查裁判规则**：证据分级、六级裁定、OTL 污染清单、人物反转表、报告模板、站内矛盾登记 |

---

## 二、检索方法（三步）

### 第 1 步：看地图
先读 `references/00-index.md` 的「高频问题 → 直达路径」与「分册索引」，锁定册号。**不要一次读全库。**

### 第 2 步：用检索脚本

```bash
python scripts/kr_lookup.py 宣统 Xuantong        # 全文检索（中英混合，多词 OR）
python scripts/kr_lookup.py --list               # 列全部册子
python scripts/kr_lookup.py --toc 04             # 看某册目录
python scripts/kr_lookup.py --read 15            # 读某册全文（配合 --limit N）
python scripts/kr_lookup.py --file               # 数据源与快照信息
```

> 脚本仅依赖标准库（Python 3.8+）。若环境无 python，改用 grep／ripgrep 直接搜 `references/` 目录。

**关键词要中英双查**：`宣统` / `Xuantong`、`萨温科夫` / `Savinkov`、`帝国公约` / `Reichspakt`。

### 第 3 步：库内未命中 → 上网补查
- 条目页：`https://kaiserreich.wiki/条目名`
- 站内搜索：`https://kaiserreich.wiki/index.php?search=关键词&fulltext=1`
- ⚠️ **该站有 Cloudflare 校验，命令行 curl／python 直连一律 403，必须用网页抓取工具（WebFetch 等）。**
- 抓取时明确要求"保留专有名词、年份、数字，不得引入页面外知识"，否则易被摘要改写失真。
- 仍查不到 → 判「无据待考」，**不臆断**。

---

## 三、回答设定问题

1. **先给结论，再给依据**（册号＋小节，或 wiki URL）。
2. **区分「已载」与「未载」**：wiki 没写的，就说没写，不要补想象。
3. **区分「开局状态」与「后续走向」**：wiki 是 1936-01-01 的百科；1936 年之后的事多为**可能性**，不是定论。
4. **人物先查反转表**：KR 大量改写真实人物的生卒与立场（见 `15` §3.3），直接套用 OTL 生平是最高频错误。
5. **中文作答，首次出现专有名词附英文原名**：`德意志帝国（German Empire）`。

---

## 四、文学作品事实核查

**动手前必读 `references/15-factcheck-standards.md`**，按其中五步执行：

1. **断言抽取**：拆成可判定的原子断言 `A1…An`，分类（设定／政治实体／人物／事件／器物／时间线／称谓）。
2. **检索定位**：查 `00-index` → 对应册 → 关键词检索 → 必要时上网。
3. **裁定**：六级用语 —— ✅ 符合设定／🟡 无据待考／🟠 设定冲突／🔴 时代错置／🔴 张冠李戴／⛔ OTL 污染；并标影响 `致命／中度／轻微`。
4. **影响分级**：是否动摇世界观底座。
5. **出报告**：用 `15` §5 的模板，逐条给依据与**可直接替换的改写建议**。

**边界**：私生活、对白、虚构人物、未记载细节属创作自由，判 🟡 不判 🟠；架空世界里"历史上不可能"不等于错误，判据是"是否符合 KR 设定"。

---

## 五、绝对禁止

- ⛔ 把 KR 当成 OTL 的变体随笔写：纳粹德国、苏联、维希法国、中华民国、土耳其共和国**均不存在**。
- ⛔ 编造人名、年份、条约、席位数字。
- ⛔ 把 wiki 未载的内容说成"设定如此"。
- ⛔ 把 `Second_American_Civil_War` 之类无正文页当作既定结局（见 `00-index` §四 已知缺口）。
- ⛔ 命令行直连 kaiserreich.wiki（会被 Cloudflare 拒），一律用网页抓取工具。

---

## 六、许可与署名

- **知识库文本**：依 **CC BY-SA 4.0** 发布。源为 [Kaiserreich Wiki](https://kaiserreich.wiki/)，其内容依 **CC BY-SA 3.0** 授权；本库为其中文摘译与结构化改写，按相同方式共享。
- **脚本代码**（`scripts/`）：**MIT**。
- **非官方声明**：本 skill 为社区非商业项目，与 Kaiserreich 开发团队、Paradox Interactive 均无隶属关系。*Kaiserreich* 及其设定归其创作者所有。
- 详细署名见仓库 `NOTICE.md`。
