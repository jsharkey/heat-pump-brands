# Methodology: how to tell whether two heat pumps are the same unit

**Hypothesis:** many ductless mini-split brands sold in North America (Carrier,
Bryant, MRCOOL, Senville, Klimaire, ...) are made by Midea (GD Midea
Air-Conditioning Equipment Co.) and only rebadged.

"Same OEM" and "identical unit" are different claims, so we keep them apart.
One OEM builds many platforms. Two brands can buy from the same factory and
still get different compressors, coils, refrigerants or firmware. Every claim
in [`EQUIVALENCE.md`](EQUIVALENCE.md) is graded on the ladder below.

## 1. Confidence ladder

| Level | Name | Meaning | Minimum evidence |
|---|---|---|---|
| **L0** | Unrelated | Different OEM | Conflicting chassis *and* parts, or a known different OEM |
| **L1** | Same OEM | Same factory or parts ecosystem | One OEM-specific part number (e.g. a GMCC compressor or Welling motor) **or** an OEM-unique firmware/error-code scheme |
| **L2** | Same platform | Same cabinet and tooling, possibly different internals | L1 + matching cabinet W×D×H (±3 mm) **and** matching shipping carton |
| **L3** | Same hardware | Interchangeable outdoor unit | L2 + same compressor model + same fan motor + net weight within ±0.3 kg + same factory charge (±10 g) + same refrigerant |
| **L4** | Confirmed identical | Proven rebadge | L3 + an independent confirmation: same AHRI/DOE/ETL certification lineage, same FCC ID on the Wi-Fi module, matching service-part numbers, or a teardown/nameplate photo |

A pair is only as strong as its weakest *required* signal. One contradiction
(e.g. a different refrigerant, or a different compressor family in the same
size) caps the pair at L2, however many other signals agree.

## 2. Signals, ranked by discriminating power

### Strong (hard to match by coincidence)
1. **Compressor model number.** Midea owns GMCC/Meizhi. Their part numbers
   follow `KS?`, `KT?`, `ASM`, `ASN`, `PA`, `EA` plus displacement plus a
   suffix, e.g. `KSK103D33UEZ3` or `KTM240D43UKT`. Gree uses its own Landa/Gree
   compressors (`QXA`, `FTz`, "G-10"). Daikin, Mitsubishi and Fujitsu use
   their own as well. An exact match including the suffix is very strong.
   Matching only the family (e.g. `KTM240D43UKT` vs `KTM240D57UMT`) is L1/L2
   evidence. Caveat: GMCC sells compressors to third parties, so a GMCC
   compressor alone does **not** prove Midea assembly.
2. **Fan-motor part numbers.** Welling, another Midea subsidiary, makes the
   DC motors. Its codes look like `ZKFN-34-10-1` or `WZDK40-38G-1`. Third
   parties buy these far less often than compressors, so they are good OEM
   evidence.
3. **Shipping-carton dimensions.** The carton is tooled per factory
   production line and rarely gets redesigned for a private-label customer.
   An exact carton match to the millimetre (e.g. 887×337×610) is close to a
   fingerprint. Exception: DIY kits with pre-charged line sets ship in larger
   boxes, so a carton *mismatch* is weak counter-evidence for those.
4. **Factory refrigerant charge and net weight.** Both depend on the coil,
   compressor and receiver. Equal values to the gram or 0.01 lb point to the
   same bill of materials, **or** to a spec sheet copied from the OEM
   datasheet, which is just as telling.
5. **Error/diagnostic-code tables.** Midea's control boards use `EC 51` (ODU
   EEPROM), `EC 52/53/54` (T3/T4/TP sensors), `EH 03` (IDU fan), `EL 0C`
   (low refrigerant), `PC 00` (IPM) and so on. A brand whose manual repeats
   that table runs Midea firmware.

### Medium
6. **Cabinet W×D×H.** Midea reuses a small set of cabinets across all its
   customers. US-market examples: 765×303×555, 805×330×554, 890×342×673,
   946×410×810 (current); 770×300×555, 800×333×554, 845×363×702 (older). Use a
   ±3 mm tolerance and check whether depth includes the valve cover; brands
   differ (e.g. Bryant 845×**320**×700 vs 845×**363**×702).
7. **Indoor-unit cabinet**, e.g. 802×189×297 or 1080×226×335.
8. **Fan blade / propeller part numbers** (`ZL-560*139*12-3KN`), coil
   geometry (rows, FPI, circuits, face area) and oil type and charge (VG74
   with exact ml).
9. **Branded feature names carried over from the OEM.** Midea uses names like
   "Follow Me" and "Gold Fin", plus remote-control models such as `RG10A`.
   These are weak on their own because names get licensed or copied.

### Weak / circumstantial
10. Matching performance numbers (SEER/HSPF/capacity range). Correlated, but
    ratings shift with indoor pairing, refrigerant and test date.
11. Document metadata: the same authoring tool, page layout or translated
    typos. Distributor DAM systems sometimes reveal the OEM; ADHQ files a
    Carrier 38MARB data book as `Midea_38MARBQ09AA3_Catalog.pdf`.
12. Anecdotes from forums or retailers.

## 3. Pitfalls

- **Same OEM ≠ same unit.** Midea built both the MOX102 (720×270×495) and the
  MOX201 (765×303×555) 9K outdoor units for the *same* Xtreme line in the same
  market.
- **Regional variants.** EU (R32, 50 Hz, 220-240 V) and US (R410A/R454B,
  60 Hz) units on the same cabinet are *platform siblings* (L2), not
  interchangeable products.
- **Refrigerant transitions.** The 2023-2025 move from R410A to R454B in the
  US produced new models in old cabinets. Compare only like-for-like
  refrigerants for L3+.
- **Copy/paste errors in brochures.** Senville lists its LETO 24K outdoor unit
  at 136.69 lb, the exact weight of Klimaire's 24K unit, but in a smaller
  cabinet. Treat it as evidence that the spec text came from a shared OEM
  datasheet, not as a physical fact.
- **Inconsistent units.** Klimaire gives "1000 g" and "38.8 oz" (1100 g) for
  the same charge. Record the number exactly as printed and flag it.
- **Unit conversions.** Imperial values are usually converted *from* mm.
  Convert back (`round(in × 25.4)`) before comparing, and allow ±3 mm.
- **Dimension order.** WxDxH, WxHxD and "WDH" are all used, sometimes
  wrongly. Check against the drawing.
- **Negative controls.** Always run a known non-Midea unit through the same
  pipeline. Here that is the Gree Livo Gen4 (732×330×556, Gree G-10
  compressor), and it matched nothing. If a control *does* cluster with
  Midea units, the signal or tolerance is too loose.

## 4. Scoring used by `tools/fingerprint.py`

Each cross-brand outdoor pair gets points:

| Evidence | Points |
|---|---|
| Same compressor model (exact) | +5 |
| Same fan-motor model (exact) | +3 |
| Same carton (±3 mm) | +3 |
| Same cabinet (±3 mm) | +2 |
| Net weight within 0.3 kg | +2 |
| Factory charge within 10 g | +2 |
| Different refrigerant | −3 |

The score is a triage tool for deciding what to check by hand. It does not
replace the ladder in section 1, which is applied manually in
`EQUIVALENCE.md`.

## 5. Workflow

1. **Collect** a product-data book, service manual or submittal (not a
   marketing flyer) for each candidate series. Save it under
   `pdfs/<brand>/` and record it in `data/sources.csv` with its URL and
   edition date.
2. **Extract** with `pdftotext -layout` and look for compressor, fan motor,
   cabinet, carton, weight, charge, oil, coil geometry and error codes.
3. **Record** one row per physical unit in `data/units.csv`, in mm/kg/g,
   citing the PDF page.
4. **Cluster** with `python3 tools/fingerprint.py`.
5. **Grade** each cluster on the ladder and update `EQUIVALENCE.md`, listing
   the evidence and any contradictions.
6. **Confirm (L4)** with independent sources:
   - **AHRI Directory** (ahridirectory.org): look for identical ratings and
     shared "outdoor unit model" lineage.
   - **DOE CCMS** (regulations.doe.gov/certification-data): basic-model
     groupings and private-labeler fields.
   - **ENERGY STAR** datasets (data.energystar.gov): brand plus model numbers
     with identical ratings.
   - **FCC ID** of the Wi-Fi dongle/module (fccid.io). Midea's grantee code
     appears on modules shipped under many brands.
   - **ETL/UL listing** (Intertek Directory / UL Product iQ): the
     "manufactured by" field often names GD Midea.
   - **Nameplate / teardown photos**: compressor label and PCB part numbers
     (Midea's 11-digit `17122000xxxxx` style).

## 6. Next data to collect

- Carrier 40MAHB and Bryant 619P indoor data (indoor cabinet and motor).
- Senville AURA/LETO and Klimaire service manuals (compressor and motor
  part numbers would lift the Senville/Klimaire cluster from L2 to L3).
- MRCOOL DIY/Advantage service manuals (compressor model).
- Other suspected Midea private labels: ICP/Comfortmaker/Heil/Tempstar
  ductless, Pioneer, Della, Cooper & Hunter, Toshiba (Carrier-Toshiba),
  Trane/American Standard entry ductless, Rheem/Ruud ductless, GE Appliances
  window heat pumps.
- More negative controls: Mitsubishi, Daikin, Fujitsu, LG.
