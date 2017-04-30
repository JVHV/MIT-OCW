
rate =
salary =
goal = 250000
r = .04
semi_annual_raise = .07
month_salary = salary/12.0
deposit = float(month_salary) * rate
savings = 0
for i in range(1, 36):
    gain = (savings * r) / 12.0
    savings = savings + gain + deposit
    if i % 6 == 0:
        deposit = deposit + (semi_annual_raise * deposit)
if DEBUG_MODE:
    print goal, savings, rate
print savings