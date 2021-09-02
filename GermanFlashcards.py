# ----------------------------------
# German Flashcards by Patt Martin -
# ----------------------------------

import os
import time
import json
import random
import GuessTheTranslation
from utilities import *

# ---------------------------------------------------------------------
# --- Starter Method ---
# ----------------------

def ___init___():
    clear_console()
    displayDataLoadMenu()



# ---------------------------------------------------------------------
# --- Main Methods ---
# --------------------

# Get the vocabulary words from a spreadsheet thats been converted into a JSON file
def displayDataLoadMenu():
    print("[0] Load vocab JSON via default path")
    print("[1] Load vocab JSON via custom path")
    try:
        dataLoadID = int(input("Select [#] to execute: "))
    except:
        print("Invalid selection was made... try again")
        displayDataLoadMenu()

    filepath = "Deutsch Vokabeln.json"

    if(dataLoadID == 1):
        filepath = input("customDataPath: ")

    germanData = GermanData()
    germanData.load_vocabulary_dict(load_json_file(filepath))

    displayMainMenu(germanData)

def displayMainMenu(germanData:GermanData):
    while True:
        print_seperator()
        print("[0] Play simple flashcards")
        print("[1] Play pick the correct one out of three")
        print("[9] Output specific card by index")

        try:
            selectionID = input("Select [#] to execute: ")
        except:
            print("Invalid selection was made... try again")

        if(selectionID == "0"):
            print("Reworking")
        elif(selectionID == "1"):
            playFindTheCorrectOne(germanData)
        elif(selectionID == "9"):
            print_specific_vocab_word(germanData)
        elif(selectionID == "~"):
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
            choice = input("Enter '~' to return or a value between 0-" + str(count) + ": ")
            # Return to main menu
            if (choice == "~"):
                return

            germanData.get_flashcard(int(choice)).print_card()
            
        except:
            print("Invalid data entry")

def playFindTheCorrectOne(vocabWords):
    print("TODO")
    print_seperator()

# ---------------------------------------------------------------------


# Run program
___init___()