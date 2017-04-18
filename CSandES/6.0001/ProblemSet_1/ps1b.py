#!/usr/bin/env python

r = .04
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise as a decimal: "))
monthly_salary = float(annual_salary / 12)
deposit = float(monthly_salary * portion_saved)
portion_down_payment = float(total_cost * .25)
current_savings = 0
months = 0
raise_counter = 0
while (current_savings < portion_down_payment):
    gain = (current_savings * r) / 12
    current_savings = current_savings + gain + deposit
    months = months + 1
    raise_counter = raise_counter + 1
    if raise_counter == 6:
        deposit = deposit + (semi_annual_raise * deposit)
        raise_counter = 0
print "Number of months: ", months

