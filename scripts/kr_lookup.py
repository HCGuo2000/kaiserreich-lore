#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""KR 知识库检索工具（离线，仅标准库）

用法：
  python kr_lookup.py 关键词 [关键词2 ...]      # 全文检索（中英混合），输出命中位置+上下文
  python kr_lookup.py --toc [册号]              # 列出册子目录（二级标题）
  python kr_lookup.py --read 册号 [--limit N]   # 读取某册全文（默认最多 400 行）
  python kr_lookup.py --list                    # 列出全部册子
  python kr_lookup.py --file                    # 查看数据源与快照信息

示例：
  python kr_lookup.py 宣统 Xuantong
  python kr_lookup.py Savinkov 萨温科夫
  python kr_lookup.py --toc 04
  python kr_lookup.py --read 15
"""
import os
import sys
import glob
import re

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

HERE = os.path.dirname(os.path.abspath(__file__))
REF_DIR = os.path.normpath(os.path.join(HERE, "..", "references"))

CTX = 1          # 上下文字行数
MAX_HITS = 60    # 单次检索最多展示命中条数


def list_books():
    return sorted(glob.glob(os.path.join(REF_DIR, "*.md")))


def book_no(path):
    return os.path.basename(path).split("-")[0]


def read_lines(path):
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.read().splitlines()


def cmd_list():
    books = list_books()
    if not books:
        print("未找到知识库文件，请检查路径：", REF_DIR)
        return
    print("知识库目录：", REF_DIR)
    print("-" * 72)
    for p in books:
        lines = read_lines(p)
        size = os.path.getsize(p)
        print(f"{os.path.basename(p):34s} {len(lines):>5d} 行  {size/1024:>7.1f} KB")
    print("-" * 72)
    print(f"共 {len(books)} 册")


def cmd_toc(no=None):
    for p in list_books():
        if no and book_no(p) != no.zfill(2):
            continue
        print("=" * 72)
        print(os.path.basename(p))
        print("=" * 72)
        for i, line in enumerate(read_lines(p), 1):
            if re.match(r"^#{1,3} ", line):
                print(f"{i:>5d}  {line}")
        print()


def cmd_read(no, limit=400):
    for p in list_books():
        if book_no(p) == no.zfill(2):
            lines = read_lines(p)
            for i, line in enumerate(lines[:limit], 1):
                print(line)
            if len(lines) > limit:
                print(f"\n……（共 {len(lines)} 行，已显示前 {limit} 行；用 --limit 调整或按需检索）")
            return
    print(f"未找到册号 {no}")


def cmd_search(terms):
    pats = [re.compile(re.escape(t), re.IGNORECASE) for t in terms]
    total = 0
    per_file = {}
    blocks = []
    for p in list_books():
        lines = read_lines(p)
        hits = []
        for idx, line in enumerate(lines):
            if any(pt.search(line) for pt in pats):
                hits.append(idx)
        if not hits:
            continue
        per_file[os.path.basename(p)] = len(hits)
        total += len(hits)
        out = [f"\n### {os.path.basename(p)}  （命中 {len(hits)} 处）"]
        shown = set()
        for idx in hits[:MAX_HITS]:
            lo, hi = max(0, idx - CTX), min(len(lines), idx + CTX + 1)
            if idx in shown:
                continue
            for j in range(lo, hi):
                if j in shown:
                    continue
                shown.add(j)
                mark = ">>" if j == idx else "  "
                text = lines[j][:400]
                out.append(f"{mark} L{j+1:<5d} {text}")
            out.append("")
        if len(hits) > MAX_HITS:
            out.append(f"……（本册另有 {len(hits)-MAX_HITS} 处未展示，建议缩小关键词）")
        blocks.append("\n".join(out))

    if total == 0:
        print(f"未命中：{' / '.join(terms)}")
        print("建议：①换用英文原名重试（如 Savinkov）；②查 00-index.md 的路由表；③上网用 WebFetch 补查 wiki。")
        return

    print(f"检索词：{' / '.join(terms)}   共命中 {total} 处，分布于 {len(per_file)} 册")
    print("-" * 72)
    for k, v in sorted(per_file.items(), key=lambda x: -x[1]):
        print(f"  {k:34s} {v:>4d} 处")
    print("\n".join(blocks))


def cmd_file():
    print("数据源：https://kaiserreich.wiki/ （官方 wiki，MediaWiki）")
    print("采集快照：2026-10-25")
    print("对应游戏版本：KR4 1.7「Crossroads of Civilisation」（2026-09-18）")
    print("知识库路径：", REF_DIR)
    print("裁判规则：见 15-factcheck-standards.md")


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return
    if args[0] in ("-h", "--help"):
        print(__doc__)
    elif args[0] == "--list":
        cmd_list()
    elif args[0] == "--toc":
        cmd_toc(args[1] if len(args) > 1 else None)
    elif args[0] == "--read":
        limit = 400
        if "--limit" in args:
            i = args.index("--limit")
            try:
                limit = int(args[i + 1])
            except Exception:
                pass
        cmd_read(args[1], limit)
    elif args[0] == "--file":
        cmd_file()
    else:
        cmd_search(args)


if __name__ == "__main__":
    main()
