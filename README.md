# Research data package — DRAFT, NOT YET PUBLISHED

**Title:** Summary tables and scenario-based calculations for a green-manufacturing case study in small-scale tofu production

**Deposit purpose:** Supplemental research-data package for the manuscript “A Feasibility-Driven Green Manufacturing Framework for Resource-Efficient Small-Scale Tofu Production” under consideration for Journal of Applied Research in Technology & Engineering (JARTE).

**Status:** Not a published dataset. No DOI has been assigned. This archive must be reviewed and approved by the authors before depositing it. It is NOT a complete raw-data release.

## Provenance
The five CSV files reproduce the aggregate numeric information reported in the user's JARTE manuscript (Tables 2, 4, 5, 6, and 7). Figures and calculations are based on the paper's existing assumptions. This package has **not** been independently verified against original measurement sheets, laboratory certificates, or accounting records. Do not describe this as independently collected measurements or raw experimental observations.

## Files
- 01_process_water_balance.csv — stage-level water and measured wastewater volumes reported per batch. Empty values mean the volume was not separately measured; they must not be treated as zero.
- 02_intervention_comparison.csv — baseline and *design-scenario* volumes for reuse, diversion, and daily water/wastewater reductions. Post-intervention values do not represent verified sustained operational measurements.
- 03_wastewater_quality_single_test.csv — before/after BOD, COD, TSS, and pH from **one 2-liter test sample** only. This is not replicated treatment efficacy or evidence of overall regulatory compliance.
- 04_economic_basecase.csv — initial investment, scenario-based annual benefits, simple payback, and benefit/investment multiples. Water price, operational costs, and market assumptions are unverified.
- 05_benefit_sensitivity.csv — deterministic scenarios assuming 100%, 75%, 50%, or 25% benefit realization.
- REPRODUCE_SUMMARY.py — independent arithmetic checks based on aggregate values. It is **not** an original data-analysis script from the field study.
- ZENODO_METADATA_DRAFT.json — deposition metadata suggestions only; not an assigned DOI or published record.

## Study scope and methodological caveats
- Single small-scale tofu enterprise in Indonesia; nominal daily production is 15 batches at approximately 14 kg soybean per batch.
- The reported water and wastewater reductions are **projections under intervention design assumptions**. They are not measured continuous-operation results.
- Reuse into product-contact stages has **not** been tested for microbial safety, odor, or product sensory properties.
- The whey-to-fertilizer pathway assumes complete allocation of whey. Actual sales, prices, market uptake, packaging, storage, registration, and steady-state operation are not validated.
- The filtration test used one sample of 2 liters: no replicate laboratory tests are available in the uploaded manuscript. BOD and COD exceeded the cited 2014 regulatory limits after filtration.
- Monetary water benefit uses an implied estimated water unit price of IDR 87.5/L = IDR 87,500/m³; **no independent source document was included**.
- The 'B/C ratio' in the manuscript is annual benefit divided by initial investment. It does not incorporate full life-cycle operating expenditures.
- Measurements were rounded in manuscript tables, so per-stage totals may differ from independently recomputed values by rounding.

## Before public publication — verification needed
1. Confirm authors' permission and ownership of the underlying records, as well as the enterprise's confidentiality agreement.
2. Obtain and review original raw volume notes, laboratory report(s), experimental methods, and economic workbook; add them only when authorized and anonymized.
3. Verify whether the draft summary values are faithful to the original thesis. Reconcile any deviations instead of silently changing published numbers.
4. Decide whether the journal accepts a **summary-only** data deposit, given its requirement for underlying research data. If not, supply de-identified raw records or ask the editor for a confidentiality exception.
5. Protect peer-review anonymity: creator metadata, affiliations, linked profiles, archive contents and file metadata can identify authors. Check journal guidance for anonymized repository links or blind-review deposits.
6. Confirm the appropriate license with all authors and the data owner. Do not assume CC BY 4.0 permission for third-party enterprise data.

## Proposed data citation after formal publication
Anonymous authors (2026). *Summary tables and scenario-based calculations for a green-manufacturing case study in small-scale tofu production* [Data set]. Zenodo. https://doi.org/[DOI TO BE ASSIGNED BY REPOSITORY]

This example is a placeholder, NOT a real DOI. Replace after Zenodo publication, and update creators with actual attribution in accordance with journal double-blind rules.
