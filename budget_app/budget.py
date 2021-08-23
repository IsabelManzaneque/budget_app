class Category:
    """
    Class used to instantiate objects based on different budget categories
    like food, clothing, and entertainment. When objects are created, they
    are passed in the name of the category

    """

    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.balance = 0.00

    def __str__(self):
        """ Implements __str__() to display statements consisting
        in a description, an amount and the account's balance """

        display = self.category.center(30, "*") + "\n"
        for entry in self.ledger:
            display += str(entry["description"]).ljust(30 - len(str(entry["amount"])))[:30 - 1-len(str("{:.2f}".format(entry["amount"])))]\
                    + " " + str("{:.2f}".format(entry["amount"])) + "\n"
        display += f"Total: {self.balance}"
        return display

    def deposit(self, amount, description=""):
        """ Deposits a certain amount into the account """

        deposit = {"amount": amount, "description": description}
        self.balance += float(amount)
        self.ledger.append(deposit)

    def withdraw(self, amount, description=""):
        """ Withdraws a certain amount from the account. If there
         are not enough funds, nothing is added to the ledger."""

        if self.check_funds(amount):
            withdraw = {"amount": - amount, "description": description}
            self.balance -= amount
            self.ledger.append(withdraw)
            return True
        return False

    def get_balance(self):
        """ Returns the account's balance"""

        return self.balance

    def transfer(self, amount, category):
        """ Withdraws an amount from the current category and
        adds a deposit to another category"""

        if self.check_funds(amount):
            self.withdraw(amount,  f"Transfer to {category.category}")
            category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        """ accepts an amount and returns False if it's greater than
        the balance of the budget category. Returns True otherwise."""

        if amount <= self.balance:
            return True
        return False


def create_spend_chart(categories):
    """Creates and returns a bar chart.

    The bar chart shows the percentage spent in each category passed into the function.
    The percentage spent is calculated only with withdrawals

    """

    aux = ""
    max_len = 0
    total_expenses = 0
    withdraws = []

    # gets a list of the withdraws per category

    for category in categories:
        aux += category.category + "\n"
        holder = 0
        for i in range(len(category.ledger)):
            if category.ledger[i].get("amount") < 0:
                holder += category.ledger[i].get("amount")
                total_expenses += category.ledger[i].get("amount")
        withdraws.append(holder)

    # converts the withdraws per category in the percentage spent

    for i in range(len(withdraws)):
        withdraws[i] = withdraws[i] * 100 / total_expenses

    # prints percentages per category and bar chart

    bar_chart = "Percentage spent by category\n"

    for i in range(100, -10, -10):
        bar_chart += str(i).rjust(3) + "|"
        for j in range(len(withdraws)):
            if withdraws[j] < i:
                bar_chart += "   "
            else:
                bar_chart += " o "
        bar_chart += "\n"
    bar_chart += "    ----------\n"

    # prints categories and bar chart

    for item in aux.split():
        if len(item) > max_len:
            max_len = len(item)

    for i in range(max_len):
        bar_chart += "     "
        for j in range(len(aux.split())):
            try:
                bar_chart += aux.split()[j][i].ljust(3)
            except IndexError:
                bar_chart += "   "
        bar_chart += "\n"

    return bar_chart
