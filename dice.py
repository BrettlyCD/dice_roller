import random
import shortuuid
from dice_db import data_entry
from plot import game_stats


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
    q = 0
    while True:
        while True:
            if q > 0: # checking if input was end program or new game, which will skip main menu.
                break
            choice = input_valid("(a) Start New Game\n(b) View Historical Stats\n(c) Close Program", 3)
            if choice == 'A':
                break
            elif choice == 'B': 
                print('This option is in development, please check-in later.')  
            else:
                q = 2
                break
        
        if q == 2: #checking from ending selection input - if selected close program, q=2, which should break from program loop
            break

        gameChoice = input_valid("(a) Settler's of Catan\n(b) Machi Koro\n(c) Other\n", 3)
        if gameChoice == 'A':
            game = game_options[0]
        elif gameChoice == 'B':
            game = game_options[1]
        elif gameChoice == 'C':
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
                next = input_valid("(a) Roll Again\n(b) Change # of Dice\n(c) End Game\n\nWhat next?: ", 3)
                if next == 'A':
                    break
                elif next == 'B':
                    dice = count_valid("Choose # of Dice: ")
                    break
                else:
                    i = 1
                    break
        while True:
            ending = input_valid("(a) Start New Game\n(b) Main Menu\n(c) View Game Stats\n(d) Exit Program\n\nWhat next?: ", 4)
            if ending == 'A':
                q = 1
                break
            elif ending == 'B':
                q = 0
                break
            elif ending == 'C':
                game_stats(str(gameID))
            else:
                q = 2
                break

run_program()