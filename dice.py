import sqlite3
import time
import datetime
import random 
#import matplotlib.pyplot as plt #importing matplotlib below to show distribution of dice rolls
#import matplotlib.dates as mdates
#from matplotlib import style
#style.use('fivethirtyeight')

start_options = ['A','B']
input_options = ['A','B','C','D']
alert = "Option not available."

def start_valid(message, i=1):
    while True:
        try:
            answer = input(message).upper()
            if answer in start_options:
                return answer
                break
            else:
                print(alert + ' Try again: ')
        except:
            print(alert + ' Try again: ')

def input_valid(message, i=1):
    while True:
        try:
            answer = input(message).upper()
            if answer in input_options:
                return answer
                break
            else:
                print(alert + ' Try again: ')
        except:
            print(alert + ' Try again: ')

def count_valid(message, i=1):
    while True:
        try:
            count = int(input(message))
            if count >= 1:
                return count
                break
        except:
            print('You must input a numerical value.' + message)

def run_program():
    while True:
        while True:
            choice = start_valid("(a) Start Rolling\n(b) View Historical Stats\n")
            if choice == 'A':
                break
            else: 
                print('This option is in development, please check-in later.')  
        dice = count_valid("Choose # of Dice: ")
        i = 0
        while True:
            if i == 1:
                break
            for x in range(int(dice)):
                print(random.randint(1,6))

            while True:
                next = input_valid("(a) Roll Again\n(b) Change # of Dice\n(c) View game stats\n(d) Exit Program\n\nWhat next?: ")
                if next == 'A':
                    break
                elif next == 'B':
                    dice = count_valid("Choose # of Dice: ")
                    break
                elif next == 'C':
                    print('This option is in development, please check-in later.')
                else:
                    i = 1
                    break
        break
                
run_program()
        






# Options = ["a","b","c"]
# def sep():
#     print("___")
# def sepline():
#     print("___\n")

# print("6 Sided Dice Simulator--\n")

# dice = input("Choose # of Dice: ")

# while True:
#     while True:
#         try:
#             if int(dice) >= 1:
#                 break
#         except:
#             print("***Input Numerical Value***")
#             dice = input("Choose # of Dice: ")
#             continue
#     while True:
#         try:
#             sep()
#             print("You rolled...")
#             for x in range(int(dice)):
#                 print(random.randint(1,6))
#             sepline()
#             break
#         except ValueError:
#             print("***Input Numerical Value***")
#             sep()
#             continue

#     prompt = str(input("(a) Roll Again\n(b) Change # of Dice\n(c) Exit Program\n\nWhat next?:"))

#     if prompt == "a":
#         continue
#     elif prompt == "b":
#         sep()
#         dice = input("Choose # of Dice: ")
#         continue
#     elif prompt == "c":
#         sep()
#         print("Thanks for playing!")
#         break
#     else:
#         print("\n***Please choose one of the following options***")
#         sep()
#         prompt = str(input("(a) Roll Again\n(b) Change # of Dice\n(c) Exit Program\n\nWhat next?: "))
#         while True:
#             if prompt == "a":
#                 break
#             elif prompt == "b":
#                 sep()
#                 dice = input("Choose # of Dice: ")
#                 break
#             elif prompt == "c":
#                 sep()
#                 print("Thanks for playing!")
#                 break
#             else:
#                 print("\n***Please choose one of the following options***")
#                 sep()
#                 prompt = str(input("(a) Roll Again\n(b) Change # of Dice\n(c) Exit Program\n\nWhat next?: "))
#                 continue
#         if prompt == "a":
#             continue
#         elif prompt == "b":
#             sep()
#             dice = input("Choose # of Dice: ")
#             continue
#         elif prompt == "c":
#             sep()
#             print("Thanks for playing!")
#             break
