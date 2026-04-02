"""
Regenerate all charts for the PSW Tax Contribution Analysis.
Fixes encoding issues and applies consistent professional styling.
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib
matplotlib.rcParams['font.family'] = 'sans-serif'

# --- Consistent style ---
BLUE = '#1e3a5f'
RED = '#b91c1c'
GREEN = '#15803d'
LIGHT_BLUE = '#3b82f6'
LIGHT_GREY = '#f1f5f9'
DARK = '#0f172a'

plt.rcParams.update({
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'axes.edgecolor': '#e2e8f0',
    'axes.grid': True,
    'grid.color': '#f1f5f9',
    'grid.linewidth': 0.8,
    'font.size': 11,
    'axes.titlesize': 14,
    'axes.titleweight': 'bold',
    'axes.labelsize': 11,
})

GBP = lambda x: f'\u00a3{x:,.0f}'

# ============================================================
# DATA
# ============================================================
employment = pd.DataFrame({
    'Employer': ['Cranswick Convenience Foods', 'Copernus Ltd'],
    'Role': ['Production Operative', 'Team Leader'],
    'Period': ['Jul 2024 \u2013 Apr 2025', 'Apr 2025 \u2013 Mar 2026'],
    'Months': [9, 12],
    'Hourly_Rate': [12.11, 14.00],
    'Gross_Earnings': [11605.28, 30534.46],
    'PAYE_Tax': [0.00, 3794.20],
    'Employee_NI': [485.34, 1513.47],
    'Employee_Pension': [214.28, 1010.60],
    'Employer_NI': [1500, 3888.91],
    'Employer_Pension': [130, 606.35],
    'Pension_Pot_Actual': [504.31, 1975.39]
})
employment['Total_Tax_NI'] = employment['PAYE_Tax'] + employment['Employee_NI']

ni_total = employment['Employee_NI'].sum()
ni_nhs_share = ni_total * 0.80
ihs_total = 2070 + 940
nhs_used = 96

# ============================================================
# CHART 1: Tax, NI & Pension by Employer
# ============================================================
fig, ax = plt.subplots(figsize=(10, 6))
x = range(len(employment))
width = 0.25
bars1 = ax.bar([i - width for i in x], employment['PAYE_Tax'], width, label='PAYE Income Tax', color=BLUE)
bars2 = ax.bar(x, employment['Employee_NI'], width, label='National Insurance', color=RED)
bars3 = ax.bar([i + width for i in x], employment['Employee_Pension'], width, label='Pension', color=GREEN)

ax.set_xticks(x)
ax.set_xticklabels(['Cranswick\n(Jul 2024 \u2013 Apr 2025)', 'Copernus\n(Apr 2025 \u2013 Mar 2026)'])
ax.set_ylabel('Amount (\u00a3)')
ax.set_title('Tax, NI and Pension Deductions by Employer')
ax.legend(frameon=True, fancybox=False, edgecolor='#e2e8f0')
ax.yaxis.set_major_formatter(mticker.StrMethodFormatter('\u00a3{x:,.0f}'))
ax.set_axisbelow(True)

for bars in [bars1, bars2, bars3]:
    for bar in bars:
        h = bar.get_height()
        if h > 0:
            ax.text(bar.get_x() + bar.get_width()/2., h + 30,
                    f'\u00a3{h:,.0f}', ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.savefig('charts/01_tax_ni_by_employer.png', dpi=200, bbox_inches='tight')
plt.close()
print('  01 done')

# ============================================================
# CHART 2: Pawan vs UK Citizen
# ============================================================
comparison = pd.DataFrame({
    'Item': ['Student Visa', 'Student IHS (2 yrs)', 'MSc Tuition (net)', 'PSW Visa', 'PSW IHS (2 yrs)', 'Biometric Fee'],
    'Pawan': [490, 940, 9400, 822, 2070, 19.20],
    'UK_Citizen': [0, 0, 9250, 0, 0, 0]
})
comparison['Extra'] = comparison['Pawan'] - comparison['UK_Citizen']
immigration_only = comparison[comparison['Extra'] > 0].copy()

fig, ax = plt.subplots(figsize=(11, 6))
y = range(len(immigration_only))
ax.barh([i + 0.15 for i in y], immigration_only['Pawan'], 0.3, label='PSW Visa Holder', color=RED)
ax.barh([i - 0.15 for i in y], immigration_only['UK_Citizen'], 0.3, label='UK Citizen', color=GREEN)
ax.set_yticks(y)
ax.set_yticklabels(immigration_only['Item'])
ax.set_xlabel('Amount (\u00a3)')
ax.set_title('Cost Comparison \u2014 Same Job, Different Price')
ax.legend(frameon=True, fancybox=False, edgecolor='#e2e8f0')
ax.xaxis.set_major_formatter(mticker.StrMethodFormatter('\u00a3{x:,.0f}'))
ax.set_axisbelow(True)
plt.tight_layout()
plt.savefig('charts/02_pawan_vs_uk_citizen.png', dpi=200, bbox_inches='tight')
plt.close()
print('  02 done')

# ============================================================
# CHART 3: NHS Double Charge
# ============================================================
nhs_data = pd.DataFrame({
    'Source': ['NI Contribution\n(NHS share)', 'Immigration Health\nSurcharge (IHS)'],
    'Amount': [ni_nhs_share, ihs_total]
})

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

colors = [BLUE, RED]
wedges, texts, autotexts = ax1.pie(
    nhs_data['Amount'], labels=nhs_data['Source'],
    autopct=lambda p: f'\u00a3{p*nhs_data["Amount"].sum()/100:,.0f}',
    colors=colors, startangle=90, textprops={'fontsize': 10}
)
for t in autotexts:
    t.set_fontweight('bold')
    t.set_color('white')
ax1.set_title('NHS Payment Breakdown', fontsize=13, fontweight='bold')

paid_vs = pd.DataFrame({
    'Category': ['Total NHS\nPayments', 'NHS Services\nConsumed'],
    'Amount': [ni_nhs_share + ihs_total, nhs_used]
})
bars = ax2.bar(paid_vs['Category'], paid_vs['Amount'], color=[RED, GREEN], width=0.45)
ax2.set_ylabel('Amount (\u00a3)')
ax2.set_title('What Was Paid vs What Was Used', fontsize=13, fontweight='bold')
ax2.yaxis.set_major_formatter(mticker.StrMethodFormatter('\u00a3{x:,.0f}'))
ax2.set_axisbelow(True)
for bar in bars:
    ax2.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 40,
             f'\u00a3{bar.get_height():,.0f}', ha='center', fontweight='bold', fontsize=13)

plt.tight_layout()
plt.savefig('charts/03_nhs_double_charge.png', dpi=200, bbox_inches='tight')
plt.close()
print('  03 done')

# ============================================================
# CHART 4: Net Contribution
# ============================================================
put_in_items = [
    ('PAYE Income Tax', 3794.20), ('National Insurance', 1998.81),
    ('Employer NI', 5389), ('Pension Contributions', 1224.88),
    ('Employer Pension', 736), ('Student Visa + IHS', 1430),
    ('PSW Visa + IHS', 2892), ('MSc Tuition (net)', 9400),
    ('VAT (est.)', 2000), ('Council Tax (est.)', 1200)
]
total_in = sum(v for _, v in put_in_items)
total_out = 96
net = total_in - total_out

fig, ax = plt.subplots(figsize=(10, 6))
categories = ['Total Contributed\nto UK Economy', 'Total Consumed\nfrom Public Services', 'Net Contribution']
values = [total_in, total_out, net]
colors_bar = [BLUE, RED, GREEN]
bars = ax.bar(categories, values, color=colors_bar, width=0.5)
ax.set_ylabel('Amount (\u00a3)')
ax.set_title('Net Fiscal Contribution to the UK (Jan 2023 \u2014 Mar 2026)')
ax.yaxis.set_major_formatter(mticker.StrMethodFormatter('\u00a3{x:,.0f}'))
ax.set_axisbelow(True)

for bar, val in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 300,
            f'\u00a3{val:,.0f}', ha='center', fontweight='bold', fontsize=14)

plt.tight_layout()
plt.savefig('charts/04_net_contribution.png', dpi=200, bbox_inches='tight')
plt.close()
print('  04 done')

# ============================================================
# CHART 5: vs UK Average
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

tax_comp = pd.DataFrame({
    'Category': ['Income Tax Paid', 'NI Paid'],
    'UK Median Earner': [4493, 2094],
    'PSW Holder': [3794, 1513]
})
x = range(len(tax_comp))
axes[0].bar([i-0.15 for i in x], tax_comp['UK Median Earner'], 0.3, label='UK Median Earner', color=BLUE)
axes[0].bar([i+0.15 for i in x], tax_comp['PSW Holder'], 0.3, label='PSW Visa Holder', color=RED)
axes[0].set_xticks(x)
axes[0].set_xticklabels(tax_comp['Category'])
axes[0].set_title('Annual Tax and NI Comparison', fontweight='bold', fontsize=13)
axes[0].legend(frameon=True, fancybox=False, edgecolor='#e2e8f0')
axes[0].yaxis.set_major_formatter(mticker.StrMethodFormatter('\u00a3{x:,.0f}'))
axes[0].set_axisbelow(True)

nhs_comp = pd.DataFrame({
    'Category': ['NHS Cost\nPer Person/Year', 'Actual NHS\nUsage/Year'],
    'Amount': [4257, 150/2.5]
})
bars2 = axes[1].bar(nhs_comp['Category'], nhs_comp['Amount'], color=[BLUE, GREEN], width=0.45)
axes[1].set_title('NHS: Average Cost vs Actual Usage', fontweight='bold', fontsize=13)
axes[1].yaxis.set_major_formatter(mticker.StrMethodFormatter('\u00a3{x:,.0f}'))
axes[1].set_axisbelow(True)
for bar in bars2:
    axes[1].text(bar.get_x() + bar.get_width()/2., bar.get_height() + 30,
                 f'\u00a3{bar.get_height():,.0f}', ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig('charts/05_vs_average_uk.png', dpi=200, bbox_inches='tight')
plt.close()
print('  05 done')

# ============================================================
# CHART 6: Pension
# ============================================================
pension = pd.DataFrame({
    'Provider': ['Cranswick (L&G)', 'Copernus'],
    'My_Contributions': [214.28, 1010.60],
    'Employer_Contributions': [130, 606.35],
    'Actual_Pot_Value': [504.31, 1975.39]
})

fig, ax = plt.subplots(figsize=(9, 5))
x = range(len(pension))
ax.bar([i-0.15 for i in x], pension['My_Contributions'], 0.3, label='Employee Contributions', color=BLUE)
ax.bar([i+0.15 for i in x], pension['Employer_Contributions'], 0.3, label='Employer Contributions', color=GREEN)
ax.scatter(x, pension['Actual_Pot_Value'], color=RED, s=120, zorder=5, label='Actual Pot Value', edgecolors='white', linewidth=2)
ax.set_xticks(x)
ax.set_xticklabels(pension['Provider'])
ax.set_title('Pension: Contributions vs Actual Value')
ax.legend(frameon=True, fancybox=False, edgecolor='#e2e8f0')
ax.yaxis.set_major_formatter(mticker.StrMethodFormatter('\u00a3{x:,.0f}'))
ax.set_axisbelow(True)

for i, row in pension.iterrows():
    ax.annotate(f'\u00a3{row["Actual_Pot_Value"]:,.0f}',
                (i, row['Actual_Pot_Value']), textcoords="offset points",
                xytext=(0, 12), ha='center', fontweight='bold', fontsize=10, color=RED)

plt.tight_layout()
plt.savefig('charts/06_pension.png', dpi=200, bbox_inches='tight')
plt.close()
print('  06 done')

print('\nAll immigration charts regenerated.')
