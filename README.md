# PSW Graduate Tax Contribution: A Data-Driven Analysis

I arrived in the UK in January 2023 to study MSc Data Analytics at Aston University, Birmingham. After graduating, I moved to Hull and started working full-time — first at Cranswick Convenience Foods, then as Team Leader at Copernus Fresh Fish. This workbook uses my real payslip data to answer one question: **how much have I actually contributed to the UK, and is what the government charges me fair?**

## My Numbers

| | Amount |
|---|---|
| Gross earnings (20 months of work) | £42,139 |
| PAYE Income Tax I paid | £3,794 |
| National Insurance I paid | £1,999 |
| Employer NI (paid because I work) | ~£5,389 |
| My pension pot (confirmed from providers) | £2,479.70 |
| Student Visa + IHS | £1,195 |
| PSW Visa + IHS | £2,892 |
| MSc Tuition (net of scholarship) | £9,400 |

## Key Findings

- **I contributed ~£30,000 to the UK** in 2.5 years (tax, NI, visa fees, tuition, VAT, council tax)
- **I consumed ~£96** in public services (one A&E visit where I waited 4 hours, then paid for my own medicine)
- **I pay for the NHS twice** — National Insurance funds the NHS, and the Immigration Health Surcharge also funds the NHS. I paid £3,669 total for NHS access. A UK citizen on the same salary paid £1,599.
- **I paid £4,087 more** than a UK citizen would pay to do the exact same job (visa + IHS + international tuition premium)
- **I have No Recourse to Public Funds** — I cannot claim Universal Credit, housing benefit, or any state support despite paying into the system
- **I applied to 20-50 data roles** — most rejected me because of my visa status. My PSW expires mid-2026.
- **My pension is £2,479.70** across Legal & General (Cranswick) and my Copernus provider

## Workbook Structure

| Sheet | What it shows |
|---|---|
| **My Story** | Employment timeline, gross pay, tax, NI, pension from real payslips |
| **Me vs UK Citizen** | Side-by-side: what I paid vs what a UK citizen pays for the same job |
| **NHS Double Charge** | I pay NI (funds NHS) AND IHS (funds NHS). Pie chart showing the overlap |
| **Net Contribution** | Everything I put in vs everything I took out. The number speaks for itself. |
| **My Pension** | Confirmed pot values from provider portals, how pension works if I leave the UK |

## Data Sources

- My payslips from Cranswick Convenience Foods (Jul 2024 - Apr 2025) and Copernus Ltd (Apr 2025 - Mar 2026)
- Pension balances confirmed from Legal & General and Copernus pension provider portals
- Home Office fee schedule for PSW and Tier 4 visas
- HMRC tax rates and NI thresholds for 2024/25 and 2025/26
- NHS Reference Costs 2022-23 (VB11Z: Type 1 A&E, no investigation = £96)
- ONS: NHS expenditure per capita (£4,257/year average)

## Real-Time Updates

This analysis is maintained in a [Google Sheets live tracker](link-to-be-added) where I update my payslip data monthly. The Jupyter notebook can be re-run at any time to regenerate all charts and the Excel report.
