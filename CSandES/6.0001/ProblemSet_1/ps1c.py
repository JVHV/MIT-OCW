def getSavings( rate, salary ):
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
    return savings
    
### Main ###

low = 0
high = 10000
ans = (low + high) / 2.0
steps = 0
target = 250000
epsilon = 100
annual_salary = float(input("Enter the starting salary: "))


while abs(float(getSavings((ans/100.0), annual_salary) - target)) > epsilon:
    steps = steps + 1
    print steps, "low =", low, " and high =", high, " and ans =", ans
    if getSavings((ans/100.0), annual_salary) > target:
        high = ans
    else:
        low = ans

    ans = (low + high) / 2.0

print "Best rate is: ", ans/100.0
print "Number of steps: ", steps
