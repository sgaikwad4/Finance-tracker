# Ask for monthly allowance and expenses in different categories
print("Welcome to the finance tracker")
allowance = float(input("What is your monthly allowance?"))
expenses = float(input("How much is your monthly spending?"))

# Calculate total expenses and remaining balance
balance = round(allowance - expenses, 2)

""" Display results
 Conditional message based on balance (depending on whether 
 you overspent or underspent or spent just the right amount, 
 write a specific message - try to be kind!)"""
if balance < 0:
    print(f"${balance}")
    print("You overspent. You need to watch how much you're spending")
else:
    print(f"You have ${balance}")