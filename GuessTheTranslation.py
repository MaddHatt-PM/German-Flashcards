from utilities import *

key__flip_rate = "flip_rate"
key__kategorie = "kategorie"
all_categories = "_all"

def play_game(germanData:GermanData):
    game_options = { key__flip_rate: 0.5, key__kategorie:all_categories  }
    
    print_seperator()
    print("Welcome to Guess the Translation!")
    print("type /exit at anytime to return to the main menu")
    print("type /options at anytime to change the kategorie or language flipping")
    
    while True:
        print_seperator()

        choice = input("Enter answer: ")

        if (choice == "/exit"):
            return

        if (choice == "/options"):
            config_options(game_options)

    return

def config_options(game_options:dict):
    return