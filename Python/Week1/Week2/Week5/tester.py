import budget

mybudget = budget.Budget(2500)
        
print("Total Funds: ", mybudget.funds)
# Add some items to the budget
mybudget.AddBudget("Books", 100)
mybudget.AddBudget("Rent", 800)
mybudget.AddBudget("Car Note", 200)

# Spend some money on items in our budget
mybudget.Spend("Books", 50)
mybudget.Spend("Rent", 800)
mybudget.Spend("Car Note", 200)

# Display the entire budget
mybudget.PrintBudget()