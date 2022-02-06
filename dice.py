import random
import shortuuid
from dice_db import data_entry


input_options = ['A','B','C','D']
game_options = ["Settlers of Catan", "Machi Koro", "Other"]
alert = "Option not available."

def input_valid(message, ind, i=1):
    while True:
        try:
            answer = input(message).upper()
            if answer in input_options[:ind]:
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
            choice = input_valid("(a) Start New Game\n(b) View Historical Stats\n", 2)
            if choice == 'A':
                break
            else: 
                print('This option is in development, please check-in later.')  

        gameChoice = input_valid("(a) Settler's of Catan\n(b) Machi Koro\n(c) Other\n", 3)
        if choice == 'A':
            game = game_options[0]
        elif choice == 'B':
            game = game_options[1]
        elif choice == 'C':
            game = game_options[2]

        gameID = str(shortuuid.uuid())

        dice = int(count_valid("Choose # of Dice: "))
        i = 0
        
        while True:
            if i == 1:
                break
            rollList = []
            for x in range(dice):
                die = random.randint(1,6)
                rollList.append(die)
                print(die)
                roll = sum(rollList)

            if __name__ == '__main__':
                data_entry(game, gameID, dice, roll)

            while True:
                next = input_valid("(a) Roll Again\n(b) Change # of Dice\n(c) View game stats\n(d) Exit Program\n\nWhat next?: ", 4)
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