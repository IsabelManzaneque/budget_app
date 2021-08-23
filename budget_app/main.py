import budget
from budget import create_spend_chart

food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food, "\n")
print(clothing, "\n")
print(create_spend_chart([food, clothing, auto]))

food = budget.Category("Food")
food.deposit(900, "deposit")
entertainment = budget.Category("Entertainment")
entertainment.deposit(900, "deposit")
business = budget.Category("Business")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

print(business, "\n")
print(food, "\n")
print(business, "\n")
print(create_spend_chart([business, food, entertainment]))




