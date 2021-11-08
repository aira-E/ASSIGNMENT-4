#Create a program that will ask for name, age and address. Display those details in the following format. Hi, my name is _____. I am ____ years old and I live in _____ .
def user_identity ():
    name = input("What is your name? ")
    age = int(input ("How old are you? "))
    if age >= 18:
        print ("You are on legal age")
    else:
        print ("You are underage")
    add = input("Where do you live? ")
    return name, age, add
def output (name, age, add):
    print(f"Hi, my name is {name}. I am {age} years old. And I live in {add}.")

name, age, add = user_identity ()
output (name,age, add)