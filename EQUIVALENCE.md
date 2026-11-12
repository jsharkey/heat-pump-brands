# Equivalency table (working draft)

Grades (L0-L4) follow [`METHODOLOGY.md`](METHODOLOGY.md). Raw numbers are in
[`data/units.csv`](data/units.csv), and `python3 tools/fingerprint.py`
regenerates the clusters. Nothing here is L4 yet; independent confirmation
(AHRI/DOE/FCC/ETL/nameplate) is still to do.

## 1. Who makes it? (brand-level verdict)

| Brand / series | Verdict | Grade | Key evidence |
|---|---|---|---|
| **Carrier 38MARB / 40MAHB** (2021-, R410A) | Midea | **L1 (strong) → L2 with Midea Xtreme** | GMCC `KSK103D33UEZ3` compressor (same part as Midea Xtreme 9K/12K); Welling `ZKFN-34-10-1` and `ZKFN-80-8-3` outdoor fan motors (same parts as Midea Xtreme); cabinet **and carton** identical to Midea Xtreme outdoor units; Midea-style EC/EH/PC error codes in SG-38MARB; distributor files the data book as `Midea_38MARBQ09AA3_Catalog.pdf` |
| **Bryant 538P\*R / 619P\*R** (2016, R410A) | Midea (likely) | **L1** | Welling `WZDK40-38G-*`, `WZDK120-38G-*`, `ZKFN-50-8-2` fan motors; GMCC `ASM98D1UFZA`/`ASM108D1UFZA`/`ASM135D23UFZ` compressors; fan blade `ZL-560*139*12-3KN` shared with Carrier 38MARB; cabinets ≈ the older Midea set (depth measured differently) |
| **MRCOOL Advantage 5th Gen** | Midea | **L2 with Carrier 38MARB** | Every size uses an exact Carrier 38MARB / Midea cabinet *and* carton (765/805/890/946 family) |
| **MRCOOL DIY 5th Gen** (R454B) | Midea | **L1 (strong)** | Cabinets match the Midea/Carrier set; error-code table (EC 51-54, EC 07, EH 00/03, EL 0C, PC 00-08) matches Carrier SG-38MARB; "Follow Me" feature name; indoor 802×189×297 shared with Klimaire and older MRCOOL. Cartons differ (DIY line-set packaging) |
| **MRCOOL DIY 3rd Gen** (R410A) | Midea | **L2 with Klimaire KSIE** | 18K: same outdoor cabinet (845×363×702), same indoor (1080×226×335), same factory charge **68.8 oz / 1950 g**. 24K: same indoor, same charge **82.9 oz / 2350 g** (different outdoor cabinet). 12K: same outdoor and indoor cabinet |
| **Klimaire KSIE / KSIV** | Midea | **L2 with Senville; L2 with MRCOOL DIY 3** | Exact cabinet and carton matches with Senville LETO/AURA (770/800/845 family); KSIE 9K net/gross weight **63.9 / 69.4 lb** identical to Senville LETO 9K |
| **Senville LETO** | Midea | **L2 with Klimaire** | See above; brochure even repeats Klimaire's 24K weight (136.69 / 147.27 lb) for a smaller cabinet, which points to a shared OEM datasheet |
| **Senville AURA** | Midea | **L2 with Klimaire (9-18K); L2 with Carrier 38MARB (24-36K)** | 24/30/36K use the 946×410×810 cabinet with factory charges **2600 / 2750 / 3400 g**, exactly Carrier 38MARBQ24/30/36's 2.60 / 2.75 / 3.40 kg |
| **Midea Xtreme** (EU, R32, 50 Hz) | Midea (reference) | n/a | Midea's own technical manual; used as the reference fingerprint |
| **Gree Livo Gen4** | Gree | **L0** (negative control) | Gree G-10 compressor; cabinets 732×330×556 and 803×351×556 match none of the Midea set |

## 2. Outdoor-unit platform map (size by size)

Rows are Midea outdoor cabinets. A model in the same row shares that
cabinet (±3 mm). **Bold** means the shipping carton also matches the row's
reference carton exactly. Other cells match the cabinet only.

### 2a. Current cabinet family (2019-)

| Cabinet W×D×H (mm) | Ref. carton (mm) | Carrier 38MARB (R410A) | Midea Xtreme EU (R32) | MRCOOL Advantage 5 | MRCOOL DIY 5 (R454B) | Senville AURA | MRCOOL DIY 3 |
|---|---|---|---|---|---|---|---|
| 765×303×555 | 887×337×610 | **38MARBQ06AA3**, **38MARBQ12AA1** (115 V) | **MOX201-09HFN8**, **MOX201-12HFN8** | **A-12-HP-C-230D-O** (+ 9K/115 V variants) | DIY-09/12-HP-C-115D25-O | – | – |
| 805×330×554 | 915×370×615 | **38MARBQ09AA3**, **38MARBQ12AA3** | **MOX301-18HFN8** | **A-18-HP-C-230D-O** | – | – | – |
| 890×342×673 | 995×398×740 | **38MARBQ18AA3** | **MOX401-24HFN8** | **A-24-HP-C-230D-O** | DIY-18-HP-C-230D25-O | – | – |
| 946×410×810 | 1090×500×885 | **38MARBQ24/30/36AA3** | – | **A-36-HP-C-230D-O** | DIY-24/36-HP-C-230D25-O | SENA-24/30/36HF/OZ (carton 875 mm high) | DIY-24/36-HP-C-230B |

Shared parts within this family:

| Part | Carrier 38MARB | Midea Xtreme EU |
|---|---|---|
| Compressor GMCC `KSK103D33UEZ3` | 06K, 12K-115V (765 cabinet) | 09K/12K MOX102 (720 cabinet) |
| Compressor GMCC `KTM240D43UKT` / `KTM240D57UMT` | 18K, 24K (`…D43UKT`) | 24K (`…D57UMT`), same family with a different suffix |
| Outdoor fan motor Welling `ZKFN-34-10-1` | 06K, 09K, 12K | MOX201-09/12, MOX301-18 |
| Outdoor fan motor Welling `ZKFN-80-8-3` | 18K | MOX401-24 |

**Reading:** Carrier's 9K and 12K (805 cabinet) are built on the platform
Midea uses for its EU 18K. Carrier's 18K uses Midea's EU 24K platform. That is
the expected pattern for one OEM tuning one cabinet for different markets and
refrigerants (L2, not L3).

### 2b. Older cabinet family (~2016-2022)

| Cabinet W×D×H (mm) | Ref. carton (mm) | Klimaire KSIE | Klimaire KSIV | Senville LETO | Senville AURA | MRCOOL DIY 3 | Bryant 538P*R* |
|---|---|---|---|---|---|---|---|
| 770×300×555 | 900×345×585 | **KSIE009-H121/H221-O** | **KSIV009-H119-O** | **SENL-09CD/O**, **SENL-12CD/O** | – | – | – |
| 800×333×554 | 920×390×615 | **KSIE012-H120/H220-O** | **KSIV012-H119/H219-O**, **KSIV018-H219-O** | **SENL-18CD/O** | **SENA-09HF/OZ**, **SENA-12HF/OZ** | DIY-12-HP-C-115B | 538PEQ009/012 (810×310×558) |
| 845×363×702 | 965×395×755 | **KSIE018-H220-O** | KSIV024-H219-O (carton 765 mm high) | **SENL-24CD/O** | **SENA-18HF/OZ** | DIY-18-HP-C-230B | 538PEQ018 (845×320×700) |

\*Bryant's figures are close but outside ±3 mm, apparently because depth is
measured without the valve cover. This needs a drawing check.

## 3. Closest pairs found so far (best L3 candidates)

| Pair | Matches | Mismatches | Grade | What would promote it |
|---|---|---|---|---|
| Klimaire KSIE009 ↔ Senville SENL-09CD | cabinet, carton, net **and** gross weight (63.9/69.4 lb) | factory charge (1000 g vs 799 g) | L2 | Compressor/fan part numbers from either service manual |
| Klimaire KSIE018 ↔ MRCOOL DIY-18 (3rd Gen) | outdoor cabinet, indoor cabinet, charge 68.8 oz | weight (45.8 vs 44.8 kg), carton (DIY packaging) | L2 | Compressor model; AHRI ratings |
| Klimaire KSIE018 ↔ Senville SENA-18HF | cabinet, carton, charge 1950 g | weight (45.8 vs 48.7 kg) | L2 | Compressor model |
| Senville SENA-24/30/36HF ↔ Carrier 38MARBQ24/30/36 | cabinet, charge (2600/2750/3400 g) | carton height (875 vs 885 mm), weight (0.5-4.4 kg apart), ratings slightly different | L2 | Senville compressor list; Carrier uses `KTM240D43UKT` / `KTF250D22UMT` |
| MRCOOL A-xx (Advantage 5) ↔ Carrier 38MARB | cabinet + carton, all four sizes | weights differ (e.g. A-12 26.8 kg vs 38MARBQ12AA1 30.3 kg) | L2 | MRCOOL compressor list; refrigerant of Advantage 5 |
| Carrier 38MARBQ12AA3 ↔ Midea MOX301-18 | cabinet, carton, fan motor, weight 33.4 vs 33.5 kg | compressor (KTN110 vs KSN140), refrigerant, capacity | L2 (platform sibling) | n/a: different products by design |

## 4. Open questions

- No **US-market Midea-branded** unit is in the dataset yet. That is the
  anchor needed to show that a US rebadge is identical (L3/L4), not just a
  platform sibling.
- Senville, Klimaire and MRCOOL spec sheets don't publish compressor or motor
  part numbers. Their service manuals probably do.
- Bryant 538P*R uses Hitachi/Highly (`DA250S2C-30MT`) and Mitsubishi
  (`TNB306FPGMC-L`) compressors in its 24K and 30K sizes, despite
  Welling motors. This is a reminder that compressor brand ≠ assembler.
