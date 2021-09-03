# ----------------------------------
# German Flashcards by Patt Martin -
# ----------------------------------
from utilities import *
import game_translate_one
import game_which_one
import game_number_translator
import game_translate_time

# ---------------------------------------------------------------------
# --- Starter Method ---
# ----------------------

def ___init___():
    clear_console()
    show_data_menu()



# ---------------------------------------------------------------------
# --- Main Methods ---
# --------------------

# Get the vocabulary words from a spreadsheet thats been converted into a JSON file
def show_data_menu():
    print("[0] Load vocab JSON via default path")
    print("[1] Load vocab JSON via custom path")
    try:
        dataLoadID = int(input("Select [#] to execute: "))
    except:
        print("Invalid selection was made... try again")
        show_data_menu()

    filepath = "Deutsch Vokabeln.json"

    if(dataLoadID == 1):
        filepath = input("customDataPath: ")

    germanData = GermanData()
    germanData.load_vocabulary_dict(load_json_file(filepath))

    show_main_menu(germanData)

def show_main_menu(germanData:GermanData):
    while True:
        print_seperator()
        print("[0] Play simple flashcards")
        print("[1] Play pick the correct one out of three")
        print("[2] Translate that number!")
        print("[3] Translate a random time!")
        print("[9] Output specific card by index")

        try:
            selectionID = input("Select [#] to execute: ")
        except:
            print("Invalid selection was made... try again")

        if(selectionID == "0"):
            game_translate_one.play_game(germanData)
        elif(selectionID == "1"):
            game_which_one.play_game(germanData)
        elif(selectionID == "2"):
            game_number_translator.play_game(germanData)
        elif(selectionID == "3"):
            game_translate_time.play_game(germanData)
        elif(selectionID == "9"):
            print_specific_vocab_word(germanData)
        elif(selectionID == "/exit"):
            print("You're already on the main menu")
            print_seperator(germanData)
        else:
            print("Invalid selection was made... try again")


# Remove later since this is just for debugging specific words
def print_specific_vocab_word(germanData:GermanData):
    count = len(germanData.vocab_words)

    while True:
        try:
            print_seperator()
            choice = input("Enter '/exit' to return or a value between 0-" + str(count) + ": ")
            # Return to main menu
            if (choice == "/exit"):
                return

            germanData.get_flashcard(int(choice)).print_card()
            
        except:
            print("Invalid data entry")


# ---------------------------------------------------------------------

# Run program
___init___()