# UK Immigration Tax Fairness Analysis

Analysis of how much a Post-Study Work (PSW) visa graduate contributes to the UK economy vs what the government charges them. Built from real payslip data across two employers over 20 months.

## The Question

A PSW graduate pays PAYE tax, National Insurance, visa fees, and Immigration Health Surcharge. A UK citizen doing the same job pays only tax and NI. Is the additional charge on immigrants fair, given their actual contribution?

## Data

- **Period**: July 2024 — March 2026 (20 months)
- **Employers**: Cranswick Convenience Foods (production), Copernus Ltd (team leader)
- **Source**: Real payslip year-to-date totals, HMRC tax tables, Home Office fee schedule
- **Gross earnings**: £42,139 over 20 months

## Workbook Structure (5 sheets)

### Sheet 1: Tax Contribution
Total PAYE tax, NI, and employer NI paid across both employers. Bar chart showing contribution by period.

### Sheet 2: Immigration Costs
Side-by-side comparison: what a PSW graduate pays vs a UK citizen for the same job. Includes visa fees, IHS, international tuition premium.

### Sheet 3: NHS Double Charge
PSW graduates pay National Insurance (which funds NHS) AND Immigration Health Surcharge (which also funds NHS). This sheet calculates the overlap. Employee NI contribution to NHS: ~£1,599. IHS paid: £2,070. Total NHS payment: £3,669 — for one A&E visit.

### Sheet 4: Net Contribution
Total money put into the UK (tax, NI, visa, tuition, VAT, council tax) vs total public services consumed (1 A&E visit). Net contribution: overwhelmingly positive.

### Sheet 5: Pension
Employee and employer pension contributions across both jobs. Notes on accessing pension if leaving the UK.

## Key Findings

- **£28,000+ contributed** to the UK economy in 20 months (tax, NI, visa, tuition, indirect taxes)
- **£150 consumed** in public services (one A&E visit, paid for own medicine)
- **£2,892 extra** paid compared to a UK citizen doing the same job (visa + IHS)
- **£2,070 IHS** is a duplicate charge — NI already funds the NHS
- **Zero benefits claimed**, no recourse to public funds
- **Net contributor**: put in approximately £28,000, took out approximately £150

## Excel Techniques Used

| Technique | Sheet |
|---|---|
| SUM, formulas | All sheets |
| Conditional formatting | Tax Contribution |
| Bar charts | Tax Contribution, Immigration Costs |
| Pie chart | NHS Double Charge |
| Cross-referencing | Net Contribution |
| Data presentation | All sheets |

## Context

This analysis was built by a PSW graduate working full-time in Hull while building a data engineering portfolio. The numbers are from real payslips. The argument is factual, not political — the data speaks for itself.
