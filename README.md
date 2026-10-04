# HSK 3.0 word list (all 9 bands): words and pinyin

The full vocabulary list of the new HSK (HSK 3.0), band by band, as clean CSV and JSON Lines files.
11,092 words: Band 1 to Band 6, plus Bands 7-9 (the advanced level, one shared list).

Published by [HSK University](https://hskuniversity.com), an online HSK course with a free plan
(HSK 3.0 Bands 1-3 and HSK 4-5, on web, Android and Windows).

- Version 1.0.0, 2026-10-04
- License: [CC BY 4.0](LICENSE) for this compilation. Credit "HSK University (hskuniversity.com)".
  The word list itself comes from a Chinese national standard; see [Where the words come from](#where-the-words-come-from).

## Files

| File | Band | Words |
|------|------|------:|
| `data/hsk30-band1.csv` | 1 | 500 |
| `data/hsk30-band2.csv` | 2 | 772 |
| `data/hsk30-band3.csv` | 3 | 973 |
| `data/hsk30-band4.csv` | 4 | 1,000 |
| `data/hsk30-band5.csv` | 5 | 1,071 |
| `data/hsk30-band6.csv` | 6 | 1,140 |
| `data/hsk30-band7-9.csv` | 7-9 | 5,636 |
| `data/all.jsonl` | all | 11,092 |

Counts are new words per band (not cumulative) and match the standard exactly.
Rows keep the order of the official list.

## Columns

| Column | Meaning |
|--------|---------|
| `id` | Stable id, e.g. `hsk30-b1-0001`, `hsk30-b79-0001`. |
| `band` | `1` to `6`, or `7-9`. |
| `word` | One plain headword in simplified Chinese, ready to use as a key. |
| `pinyin` | Pinyin of `word`, with tone marks (tone changes such as 不 bù/bú are not marked). |
| `official_entry` | The entry exactly as the standard prints it. |
| `official_pinyin` | Its pinyin exactly as published. |

`word` differs from `official_entry` in 37 rows, where the standard uses notation:

- **Variants** `爸爸|爸`: `word` keeps the first form (`爸爸`).
- **Examples** `们（朋友们）`, `员（服务员）`: `word` keeps the head (`们`, `员`).
- **Optional characters** `有（一）点儿`, `好（不）容易`: `word` drops them (`有点儿`, `好容易`).

Some strings appear more than once (89 of them in more than one band), because the standard lists a
word again for another meaning. If you use the list to check a text's level, take the lowest band.

There are no translations. Glosses are not part of the standard, so none are included.

## Where the words come from

- The list is the vocabulary appendix of *Chinese Proficiency Grading Standards for International
  Chinese Language Education* (国际中文教育中文水平等级标准, GF 0025-2021), published in 2021 by China's
  Ministry of Education and State Language Commission. It defines the bands of the new HSK, whose
  exams start worldwide on 2026-12-13 (Chinese Testing International).
- The machine-readable text is taken from [ivankra/hsk30](https://github.com/ivankra/hsk30)
  (MIT License; its notice is in [NOTICE](NOTICE)), which uses Pleco's proof-read OCR of the official
  PDF with pinyin from the chinesetest.cn word database.
- The band counts match the standard exactly, and the words match Pleco's OCR
  ([elkmovie/hsk30](https://github.com/elkmovie/hsk30), the source of ivankra's words) apart from sense-number marks.
- `scripts/build.py` rebuilds `data/` from `source/hsk30-official.csv`.

Found a mistake? Open an issue.
