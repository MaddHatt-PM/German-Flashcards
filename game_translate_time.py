from utilities import *
import random

key__time_type = "time_type"
time_type_names = { "military", "12 hour" }

def config_options(germanData:GermanData, gameOptions:tuple) -> tuple:
    return gameOptions

def play_game(germanData:GermanData):
    game_options = { key__time_type: True }
    correct_count = 0
    card_count = 0
    
    print_seperator()
    print("Welcome to Guess the Translation!")
    print("type /exit at anytime to return to the main menu")
    print("type /options at anytime to change the kategorie or language flipping")
    

    while True:
        print_seperator()
        chosen_time = time_deutsch(random.randint(0,23), random.randint(0, 59))
        choice = input("What is " + chosen_time.print_to_standard(game_options[key__time_type]) + " in Deutsch? \n")

        if (choice == "/exit"):
            return

        if (choice == "/options"):
            game_options = config_options(germanData, game_options)
            continue

        if (choice.lower() == chosen_time.print_to_deutsch().lower()):
            print("Correct")
        else:
            print("Incorrect, the correct answer was: " + chosen_time.print_to_deutsch())
            if(input("Mark as correct anyways? Y or type the answer to advance: ") == 'Y'):
                correct_count += 1

        card_count += 1
        print("Card's played: ", str(card_count)," Correct Responses: ", str(correct_count))


class time_deutsch:
    def __init__(self, hours:int, minutes:int):
        self.hours = hours
        self.minutes = minutes

    def print_to_standard(self, military_time = True):
        if (military_time == False):
            print("Program later")

        return str(self.hours) + ':' + str(self.minutes).zfill(2)


    def print_to_deutsch(self, military_time = True):
        if (military_time == False):
            print("Program later")
        
        return int_to_deutsch(self.hours) + " Uhr " + int_to_deutsch(self.minutes)
        