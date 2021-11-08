#Create a program that will ask how many apples and oranges you want to buy. Display the total amount you need to pay if apple price is 20 pesos and orange is 25. Display the output in the following format. The total amount is ______.
def groceries ():
    apple = int (input ("How many apples you wish to buy? "))
    orange = int (input ("How many oranges you wish to buy? "))
    return apple, orange

def price (apple, orange):
    apple_price = apple*20
    orange_price = orange*25
    total = apple_price + orange_price
    return apple_price, orange_price, total

def display (apple_price, orange_price, total):
    print (f"The total amount of your groceries cost {total} pesos.")
 
apple, orange = groceries ()
apple_price, orange_price, total = price (apple, orange)
display (apple_price, orange_price, total)