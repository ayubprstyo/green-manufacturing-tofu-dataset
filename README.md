# Supporting research tables — summary-level dataset

**Title:** Summary tables and scenario-based calculations for a green-manufacturing case study in small-scale tofu production

**Scope:** Supporting material for the study titled *A Feasibility-Driven Green Manufacturing Framework for Resource-Efficient Small-Scale Tofu Production*.

## About this archive
This archive presents aggregate results transcribed from the manuscript tables, accompanied by a script that reproduces selected arithmetic calculations. **It is not the original field notebook, instrument output, laboratory report, accounting workbook, or independently validated raw dataset.** It is not evidence that projected interventions were operated continuously. The original records were not supplied when this package was assembled.

The depositor provided the Zenodo record URL https://zenodo.org/records/23609064 and version-specific DOI https://doi.org/10.5281/zenodo.23609064. **The record metadata, published file contents, and DOI resolution have not been independently verified here.** If these files are deposited as a *new version* rather than edited in place, Zenodo will issue a separate version DOI; cite the DOI of the version that actually contains the files used.

## Contents and provenance
- `01_process_water_balance.csv` — stage-level volume summaries (manuscript Table 2); blank entries mean *not separately measured*, not zero.
- `02_intervention_comparison.csv` — water/wastewater baseline and **design-scenario** comparison (Table 4); post-intervention values are projections.
- `03_wastewater_quality_single_test.csv` — BOD, COD, TSS and pH from a **single 2 L sample** (Table 5), not replicated evidence of regulatory compliance.
- `04_economic_basecase.csv` — simplified investment and annual-benefit estimates (Table 6), not verified accounting records.
- `05_benefit_sensitivity.csv` — deterministic benefit-realization scenarios (Table 7).
- `REPRODUCE_SUMMARY.py` — arithmetic verification script created from manuscript summaries; not the original field-analysis script.
- `DATASET_DESCRIPTION.json` — descriptive metadata for this archive; journal/repository metadata should be managed on the Zenodo record itself.

## Calculation assumptions and important limitations
- Nominal throughput: approximately 14 kg soybeans/batch and 15 batches/day.
- Freshwater and wastewater totals are sums of rounded reported process-stage measurements. No independent raw field records were included.
- Reuse of soaking/washing water in food-contact stages **has not been validated** for microbial safety, odor or sensory effects.
- The entire whey stream allocated to liquid fertilizer represents a **design assumption**, not established production, regulatory clearance, or market acceptance.
- The single 2 L preliminary-filtration test is not evidence of stable treatment efficiency; BOD and COD remained above the cited limits.
- The base-case avoided-water-cost calculation uses an implied cost of IDR 87,500/m³; its actual source and suitability to the enterprise are unverified. Media replacement, power, and labor for water reuse were excluded.
- Fertilizer revenue and net cash flow are scenario assumptions; the market and input-cost breakdowns were not independently checked.
- The so-called B/C values divide annual benefits by initial investment; they are *not* comprehensive discounted life-cycle benefit–cost ratios.
- The files contain results reconstructed from manuscript summary tables, **not a full underlying research dataset**.

## Prior to journal use or unrestricted release
Confirm enterprise permission, validate the original laboratory report and underlying measurement and economic records, and check with the journal whether summary-only material meets its research data policy. Confirm correct repository resource type and licensing. For double-anonymous peer review, review creator metadata, linked GitHub accounts, file histories, and the public repository landing page: removing names from this ZIP alone does not anonymize a public Zenodo/GitHub record.

## Reproducibility
Place all files in one directory and run `python REPRODUCE_SUMMARY.py`. This checks the arithmetic underlying selected aggregate indicators, **not the accuracy of original observations**.
