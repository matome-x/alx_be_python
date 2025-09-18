#  financial details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Assume an annual interest rate of 5%
interest_rate = 0.05

# Project annual savings including interest
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * interest_rate)

# Display results
print(f"Your monthly savings are: {monthly_savings}")
print(f"Your projected annual savings after interest are: {projected_savings}")
