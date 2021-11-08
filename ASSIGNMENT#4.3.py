#Create a program which you will enter the amount of money you have, it will also ask for the price of an apple. Display the maximum number of apples that you can buy and the remaining money that you will have. Display the output in the following format. You can buy ___ apples and your change is ___ pesos.
def costumer_input ():
    money = int (input("How much money do you have? "))
    apple_price = int (input("How much for an apple? "))
    return money, apple_price

def cashier_output (money, apple_price):
    maximum_apples = (money/apple_price)
    change = money-(apple_price*maximum_apples)    
    return maximum_apples, change

def display (maximum_apples, change):
    print (f"You can buy {maximum_apples} apples, having {change} change")
    
money, apple_price = costumer_input ()
maximum_apples, change = cashier_output (money, apple_price)
display (maximum_apples, change)