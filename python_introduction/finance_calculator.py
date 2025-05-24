#user input for financial details
monthly_income = int(input("Enter your monthly income:"))
monthly_expense = int(input("Enter your total monthly expense:"))

#calculate monthly savings
monthly_savings = monthly_income - monthly_expense

#project annual savings
annual_rate = 0.05
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_rate)

print(monthly_savings)
print(projected_savings)
