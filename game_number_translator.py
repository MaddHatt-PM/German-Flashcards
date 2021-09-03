from utilities import *
import time
import random


def play_game(germanData:GermanData):
    correct_count = 0
    card_count = 0

    print_seperator()
    print("Welcome to Translate that Number!")
    print("type /exit at anytime to return to the main menu")

    while True:
        print_seperator()
        
        selectedNumber = random.randint(0, 4)
        answer = int_to_deutsch(selectedNumber)

        choice = input("What is the german translation of: " + str(selectedNumber) +"\n")

        if (choice == "/exit"):
            return

        if (choice.lower() == answer.lower()):
            print("Correct")
        else:
            print("Incorrect, the correct answer was: " + answer)
            if(input("Mark as correct anyways? Y or type the answer to advance: ") == 'Y'):
                correct_count += 1
        
        card_count += 1
        print("Card's played: ", str(card_count)," Correct Responses: ", str(correct_count))