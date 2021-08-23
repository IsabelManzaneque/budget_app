# budget_app
Displays an account's statements consisting in a description, an amount and a bar chart
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
## General info

This module consists in a function and a class. The class instantiates objects based on different budget categories like food, clothing, and entertainment. It contains the following methods: 

* A `deposit` method that accepts an amount and description. If no description is given, it should default to an empty string. 
* A `withdraw` method that is similar to the `deposit` method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. Returns True if the withdrawal took place, and False otherwise.
* A `get_balance` method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
* A `transfer` method that accepts an amount and another budget category as arguments. The method add withdraws an amount from the current category and then deposits it into another budget category. If there are not enough funds, nothing is added to either ledgers. This method should return True if the transfer took place, and False otherwise.
* A `check_funds` method that accepts an amount as an argument. It returns False if the a This method should be used by both the `withdraw` method and `transfer` method.

When the budget object is printed it displays:
* A title line of  the name of the category.
* A list of the items in the ledger each consisting in a description and an amount.
* A line displaying the category total.
```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

The function `create_spend_chart` takes a list of categories as an argument and it returns a bar chart that show the percentage spent in each category passed in to the function.

```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```
## Technologies
Project is created with:
* Python 3.9.6
* PyCharm Community Edition 2021.1.2 x64
## Setup
To run this project in PyCharm:

```
Download .zip
Edit files with PyCharm

