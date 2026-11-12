#!/usr/bin/env python3
"""Group heat-pump units by physical/part fingerprints.

Reads data/units.csv and prints:
  1. chassis clusters  - units whose cabinet W x D x H match within a tolerance
  2. carton clusters   - units whose shipping-box dimensions match (stronger:
                         boxes are tooled per factory)
  3. shared parts      - compressor / fan-motor part numbers seen in >1 brand
  4. pairwise scores   - cross-brand outdoor-unit pairs scored per METHODOLOGY.md

Usage:  python3 tools/fingerprint.py [--tol MM] [--min-score N]
Stdlib only.
"""
import argparse
import csv
import itertools
import os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
UNITS = os.path.join(HERE, "..", "data", "units.csv")


def num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def dims(u, prefix=""):
    d = tuple(num(u[f"{prefix}{k}_mm"]) for k in ("w", "d", "h"))
    return d if all(d) else None


def close(a, b, tol):
    return a and b and all(abs(x - y) <= tol for x, y in zip(a, b))


def cluster(units, key, tol):
    groups = []
    for u in units:
        k = key(u)
        if not k:
            continue
        for g in groups:
            if close(g["key"], k, tol):
                g["members"].append(u)
                break
        else:
            groups.append({"key": k, "members": [u]})
    return [g for g in groups if len({m["brand"] for m in g["members"]}) > 1]


def score(a, b, tol):
    """Evidence score for two outdoor units (see METHODOLOGY.md section 4)."""
    s, why = 0, []
    if a["compressor"] and a["compressor"] == b["compressor"]:
        s += 5; why.append("compressor=" + a["compressor"])
    if a["fan_motor"] and a["fan_motor"] == b["fan_motor"]:
        s += 3; why.append("fan_motor=" + a["fan_motor"])
    if close(dims(a), dims(b), tol):
        s += 2; why.append("chassis")
    if close(dims(a, "pkg_"), dims(b, "pkg_"), tol):
        s += 3; why.append("carton")
    wa, wb = num(a["net_kg"]), num(b["net_kg"])
    if wa and wb and abs(wa - wb) <= 0.3:
        s += 2; why.append(f"weight~{wa}kg")
    ca, cb = num(a["charge_g"]), num(b["charge_g"])
    if ca and cb and abs(ca - cb) <= 10:
        s += 2; why.append(f"charge~{int(ca)}g")
    if a["refrigerant"] and b["refrigerant"] and a["refrigerant"] != b["refrigerant"]:
        s -= 3; why.append("DIFFERENT refrigerant")
    return s, why


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tol", type=float, default=3.0, help="dimension tolerance, mm")
    ap.add_argument("--min-score", type=int, default=5)
    args = ap.parse_args()

    units = list(csv.DictReader(open(UNITS, newline="")))
    out = [u for u in units if u["role"] == "outdoor"]
    ind = [u for u in units if u["role"] == "indoor"]

    for title, pool, key in (
        ("OUTDOOR CHASSIS (W x D x H)", out, dims),
        ("OUTDOOR CARTON", out, lambda u: dims(u, "pkg_")),
        ("INDOOR CHASSIS (W x D x H)", ind, dims),
    ):
        print(f"\n== {title} clusters spanning >1 brand (tol {args.tol} mm) ==")
        for g in cluster(pool, key, args.tol):
            k = "x".join(str(int(x)) for x in g["key"])
            print(f"  {k}:")
            for m in g["members"]:
                print(f"     {m['brand']:<9} {m['series']:<18} {m['model']:<24} {m['refrigerant']}")

    print("\n== Part numbers shared across brands ==")
    for col in ("compressor", "fan_motor"):
        seen = defaultdict(set)
        for u in out:
            if u[col]:
                seen[u[col]].add(f"{u['brand']} {u['model']}")
        for part, who in sorted(seen.items()):
            if len({w.split()[0] for w in who}) > 1:
                print(f"  {col} {part}: " + ", ".join(sorted(who)))

    print(f"\n== Cross-brand outdoor pairs with score >= {args.min_score} ==")
    rows = []
    for a, b in itertools.combinations(out, 2):
        if a["brand"] == b["brand"]:
            continue
        s, why = score(a, b, args.tol)
        if s >= args.min_score:
            rows.append((s, a, b, why))
    for s, a, b, why in sorted(rows, key=lambda r: -r[0]):
        print(f"  {s:>2}  {a['brand']} {a['model']}  <->  {b['brand']} {b['model']}   [{'; '.join(why)}]")


if __name__ == "__main__":
    main()
