# heat-pump-brands

Are many mini-split heat pump brands just rebadged Midea units? This repo
collects manufacturer PDFs, extracts hardware fingerprints (compressor and
fan-motor part numbers, cabinet and carton dimensions, weights, refrigerant
charge, error codes) and maps equivalent models across brands.

| File | What it is |
|---|---|
| [`METHODOLOGY.md`](METHODOLOGY.md) | How we decide two units are the same: evidence ladder L0-L4, ranked signals, pitfalls, workflow |
| [`EQUIVALENCE.md`](EQUIVALENCE.md) | The equivalency table so far |
| [`data/units.csv`](data/units.csv) | One row per physical unit, normalized to mm / kg / g, with source page |
| [`data/sources.csv`](data/sources.csv) | Inventory of the PDFs with original URLs and editions |
| [`pdfs/`](pdfs/) | The source documents, by brand |
| [`tools/fingerprint.py`](tools/fingerprint.py) | Clusters units by cabinet, carton and shared parts, and scores cross-brand pairs |

```bash
python3 tools/fingerprint.py            # default: ±3 mm, show pairs scoring ≥5
```

```bash
python3 tools/fingerprint.py --tol 5 --min-score 7
```

## Headline findings (draft)

- **Carrier 38MARB** outdoor units use Midea-group parts: a GMCC
  `KSK103D33UEZ3` compressor and Welling `ZKFN-34-10-1` / `ZKFN-80-8-3` fan
  motors. These are the same part numbers as in Midea's own Xtreme
  technical manual. Their cabinets *and shipping cartons* match Midea's to
  the millimetre.
- **MRCOOL Advantage 5th Gen** uses the same cabinet and carton as Carrier
  38MARB in all four sizes. **MRCOOL DIY 5th Gen** shares the cabinets and
  the Midea error-code table.
- **Klimaire KSIE/KSIV**, **Senville LETO/AURA** and **MRCOOL DIY 3rd Gen**
  share an older Midea cabinet family, with several exact weight and
  refrigerant-charge matches.
- The **Gree Livo** negative control matches nothing, which suggests the
  fingerprints separate OEMs.

See `EQUIVALENCE.md` for grades and caveats. Nothing is proven identical
(L4) yet.

PDFs are third-party copyrighted documents, kept here for research and
cross-referencing. Original URLs are in `data/sources.csv`.
