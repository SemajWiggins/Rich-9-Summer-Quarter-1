# The amount of money we have to spend
funds = 2500

# A dictionary of our items we are spending our budget on
# The key is the name of the item; the value is the budget amount for that items
budgets = {}

# A dictionary of the expense of each budgeted item
# The key is the name of the item, the value is the amount spent on the item.
expenses = {}

# Adds an item to the budgets dictionary
def AddBudget(name, amount):
    global funds
    if name in budgets: # if the key is already in our budgets dictionary
        raise ValueError("Budget for item already exists")
    if amount > funds:
        raise ValueError("No can do, you brokie")
    budgets[name] = amount # Adds the budgeted item ot the budgets dictionary
    funds = funds - amount # Subtracts the amount from the funds
    expenses[name] = 0 # Add the budgeted item ti the expenses dictionary
    return funds

def Spend(name, amount):
    if name not in expenses:
        raise ValueError("Item not in budget")
    expenses[name] 
    budgeted = budgets[name]
    spent = expenses[name]
    return budgeted - spent

def PrintBudget():
    for name in budgets:
        budgeted = budgets[name] # Store the amount associated with that key 
        spent = expenses[name] # Store the amount on that given item
        remainingBudget = budgeted - spent
        print(f'{name:15s}, {budgeted:10.2f}, {spent:10.2f}, {remainingBudget:10.2f}')




print("Total Funds: ", funds)
# Add some items to the budget
AddBudget("Books", 100)
AddBudget("Rent", 800)
AddBudget("Car Note", 200)

# Spend some money on items in our budget
Spend("Books", 50)
Spend("Rent", 800)
Spend("Car Note", 200)

# Display the entire budget
PrintBudget