"""
Gross Salary Calculator
Calculates gross salary from basic salary by adding allowances and deducting provident fund.
Formula: Gross Salary = Basic + HRA + DA - PF
Where:
- HRA (House Rent Allowance) = 10% of basic
- DA (Dearness Allowance) = 5% of basic  
- PF (Provident Fund) = 80% of basic
"""

basic = float(input("Enter basic salary to get your gross salary: "))
hra = 0.1 * basic
da = 0.05 * basic
pf = 0.8 * basic
gross_sal = hra + da + basic - pf
print("gross salary:", gross_sal)
