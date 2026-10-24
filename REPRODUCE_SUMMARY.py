#!/usr/bin/env python3
"""Reproduce selected aggregate math from the manuscript; not field-analysis code."""
import csv
from pathlib import Path
root = Path(__file__).resolve().parent
with (root/'01_process_water_balance.csv').open(encoding='utf-8-sig', newline='') as f:
    stages=list(csv.DictReader(f))
fresh=sum(float(x['freshwater_l_per_batch']) for x in stages if x['freshwater_l_per_batch'])
ww=sum(float(x['measured_wastewater_l_per_batch']) for x in stages if x['measured_wastewater_l_per_batch'])
reused_per_batch=35.325+39.250
whey_per_batch=58.875
print('Baseline freshwater L/batch:', round(fresh,3))
print('Baseline measured wastewater L/batch:', round(ww,3))
print('Baseline freshwater L/day:', round(fresh*15,3))
print('Baseline measured wastewater L/day:', round(ww*15,3))
print('Scenario freshwater L/day:', round((fresh-reused_per_batch)*15,3))
print('Scenario measured wastewater L/day:', round((ww-reused_per_batch-whey_per_batch)*15,3))
print('Freshwater reduction:', round(100*reused_per_batch/fresh,2),'%')
print('Wastewater reduction:', round(100*(reused_per_batch+whey_per_batch)/ww,2),'%')
print('Annual water avoided cost (IDR):', round(reused_per_batch*15*87.5*365,2))
assert abs(fresh-391.588)<1e-4 and abs(ww-209.572)<1e-4
# Full annual net fertilizer benefit cannot be reconstructed without raw price/cost inputs.
