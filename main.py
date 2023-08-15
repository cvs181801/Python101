import re
#hi hi hi
#python 101
# print("HeY")
# print("This is python")
# #we are praticing python

# #multiline string:
# print("""This is line one 
# this is line two
# this is line three""")

# #concat:      
# print("I am awesome \n" + "and so are you \n" + "let's toast!")
# # \n within a regular string will create a line break

# #Print multiple strings
# print("some stuff\n" * 10)

#the input funtion
#anything passed into input() gets converted to a string.


def take_order_calculate_total():
        print("Welcome, " + name + "!")
        class Drink:
            def __init__(self, index, drinkName, price):
                self.index = index
                self.drinkName = drinkName
                self.price = price

        menu = []

        menu.append(Drink(1, "House coffee, regular", 3.25))
        menu.append(Drink(2, "House coffee, decaf", 3.25))
        menu.append(Drink(3, "Latte", 4.95))
        menu.append(Drink(4, "Mocha", 5.25))
        menu.append(Drink(5, "Cappucino", 5.00))
        menu.append(Drink(6, "Americano", 4.50))
        menu.append(Drink(7, "Hot Chocolate", 3.95))
        menu.append(Drink(8, "Steamed Cider", 3.95))
        menu.append(Drink(9, "Steamed Milk", 3.95))

        confirmation = False
        while confirmation != "Y":

            print("""Here is our menu:""")

            for drink in menu:
                print("{} : {}. ${}".format(drink.index, drink.drinkName, drink.price))

            print("""I can take your order when you're ready; please simply a sentence containing the number(s) for the drinks you want to order, for example: "6 and 7".  :) """)

            customerOrder = input()

            print("Would you like to add whip cream to any of the drinks in your order for only 1$ extra per drink? If yes, simply enter which drinks you want to add whip to using a sentence such as '6 and 7'. If no, simply enter N.")

            wantsWhip = input()

            drinksWithWhip = re.findall(r'\d+', wantsWhip)

            drinkOrder = re.findall(r'\d+', customerOrder) #and check to make sure result is not none

            print("Thank you! Please type Y to confirm if your order is correct:")
            for item in drinkOrder:
                order = int(item)
                orderIndex = menu[order - 1]
                if item in drinksWithWhip:
                    addWhip = "Yes"
                else: 
                    addWhip = "No"
                print("{} : ${}. Add whip for $1? : {}".format(orderIndex.drinkName, orderIndex.price, addWhip))
            confirmation = input()
            if input() == "Y":
                confirmation = True

        sum = 0 + len(drinksWithWhip)
        for item in drinkOrder:
            order = int(item)
            orderIndex = menu[order - 1]
            sum = sum + orderIndex.price
        print("Your total is $" + str(sum) + ".")
        print("Thank you, enjoy!")



name = input("May I have your name? (enter your name) ")
if name == "Ben" or name == "Patricia":
    print("Ok, are you evil? Type Y or N.")
    response = input()
    if response == "Y":
        print("How many good deeds have you done today?")
        response = input()
        if int(response) >= 4:
            print("Ok, come on in.")
            take_order_calculate_total()
        else:
            print("GET OUT!!!")
            exit()
    elif response != "Y":
        print("Ok, I guess you can order.")
        take_order_calculate_total()
else: # or your could use the exit() function above to stop the rest of the code from running.
    take_order_calculate_total()
    
#variables and types
# name2 = "Fruity"
# age = 17
# freakerAge = 17.89
# print(type(freakerAge))
# difference = 6 - 5
# print(difference)
# sum = 6 + 6
# remainder = 8/2 # the result of a division caluclation will be a float
# print(remainder)

# #yes, python operates according to PEMDAS!
# exponent = 2**2 #(aka 2 squared)
# print(exponent)

################
#classes and objects
################
# class Student(object):
#     name = ""
#     age = 0
#     major = ""

#     # The class "constructor" - It's actually an initializer 
#     def __init__(self, name, age, major):
#         self.name = name
#         self.age = age
#         self.major = major

# def make_student(name, age, major):
#     student = Student(name, age, major)
#     return student
# Note that even though one of the principles in Python's philosophy is "there should be one—and preferably only one—obvious way to do it", there are still multiple ways to do this. You can also use the two following snippets of code to take advantage of Python's dynamic capabilities:
# class Student(object):
#     name = ""
#     age = 0
#     major = ""

# def make_student(name, age, major):
#     student = Student()
#     student.name = name
#     student.age = age
#     student.major = major
#     # Note: I didn't need to create a variable in the class definition before doing this.
#     student.gpa = float(4.0)
#     return student
# I prefer the former, but there are instances where the latter can be useful – one being when working with document databases like MongoDB.
# --Wulfram
###############
#lists
###############
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# studentList = []
# studentList.append(Student("Alex", 20))
# studentList.append(Student("Bob", 21))
# studentList.append(Student("Ira", 15))

# for student in studentList:
#     print("Name : {}, Age : {}".format(student.name, student.age))

