"""Rebuild data/ from source/hsk30-official.csv.

source/hsk30-official.csv has band, simplified, pinyin, source_row: the vocabulary of the standard
GF 0025-2021, from ivankra/hsk30 (MIT, see NOTICE). Words and pinyin only, no translations.

Run: python scripts/build.py
"""
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "source" / "hsk30-official.csv"
BANDS = ["1", "2", "3", "4", "5", "6", "7"]
BAND_LABEL = {b: b for b in BANDS[:6]} | {"7": "7-9"}
EXPECTED = {"1": 500, "2": 772, "3": 973, "4": 1000, "5": 1071, "6": 1140, "7": 5636}
COLUMNS = ["id", "band", "word", "pinyin", "official_entry", "official_pinyin"]

PAREN_ZH = re.compile(r"（([^）]*)）")
PAREN_PY = re.compile(r"\s*\(([^)]*)\)")


def headword(entry, pinyin):
    """Turn an official entry into one plain word + pinyin.

    The standard writes variants as 爸爸|爸, examples as 们（朋友们） and optional characters as
    有（一）些. Variants keep the first form; examples keep the head; optional characters drop out.
    """
    word, py = entry.split("|")[0], pinyin.split("|")[0]
    m = PAREN_ZH.search(word)
    if m:
        head = PAREN_ZH.sub("", word)
        if head.strip("…") in m.group(1):
            word, py = head, py.split("(")[0]
        else:
            word, py = head, PAREN_PY.sub("", py)
    return word.strip(), py.strip()


def build_rows():
    rows = list(csv.DictReader(SOURCE.open(encoding="utf-8-sig")))
    out, counters = [], {b: 0 for b in BANDS}
    for r in rows:
        band = r["band"]
        counters[band] += 1
        word, py = headword(r["simplified"], r["pinyin"])
        out.append({
            "id": f"hsk30-b{BAND_LABEL[band].replace('-', '')}-{counters[band]:04d}",
            "band": BAND_LABEL[band],
            "word": word,
            "pinyin": py,
            "official_entry": r["simplified"],
            "official_pinyin": r["pinyin"],
        })
    if counters != EXPECTED:
        sys.exit(f"band counts {counters} differ from the standard {EXPECTED}")
    if len({x["id"] for x in out}) != len(out) or any(not x["word"] or not x["pinyin"] for x in out):
        sys.exit("duplicate id or empty word/pinyin")
    return out


def main():
    out = build_rows()
    data = ROOT / "data"
    data.mkdir(exist_ok=True)
    for band in BANDS:
        name = "hsk30-band7-9.csv" if band == "7" else f"hsk30-band{band}.csv"
        with (data / name).open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=COLUMNS, lineterminator="\n")
            w.writeheader()
            w.writerows(x for x in out if x["band"] == BAND_LABEL[band])
    with (data / "all.jsonl").open("w", encoding="utf-8", newline="\n") as f:
        for x in out:
            f.write(json.dumps(x, ensure_ascii=False) + "\n")
    print(f"{len(out)} words written to data/")


if __name__ == "__main__":
    main()
