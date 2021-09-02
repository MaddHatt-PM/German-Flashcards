# ----------------------------------
# German Flashcards by Patt Martin -
# ----------------------------------

import os
import time
import json
import random
# import GuessTheTranslation
import utilities

# Starter method


def ___init___():
    utilities.clear_console()
    displayDataLoadMenu()


# ---------------------------------------------------------------------
# --- Helper Methods ---
# ----------------------
def printFlashCard(flashcard:dict):
    if (len(str(flashcard[key_gender])) != 0):
        print(key_gender + ": " + flashcard[key_gender])
    if (len(str(flashcard[key_wort_deutsch])) != 0):
        print(key_wort_deutsch + ": " + flashcard[key_wort_deutsch])
    if (len(str(flashcard[id_englisch])) != 0):
        print(id_englisch + ": " + flashcard[id_englisch])
    if (len(str(flashcard[id_kategorie])) != 0):
        print(id_kategorie + ": " + flashcard[id_kategorie])


# ---------------------------------------------------------------------
# --- Main Methods ---
# --------------------

default_data_path = "Deutsch Vokabeln.json"
# Identifier variables from my spreadsheet, custom ones aren't going to work
key_gender = "Gender"
key_wort_deutsch = "Wort Deutsch"
id_englisch = "Englisch"
id_kategorie = "Kategorie"


# Get the vocabulary words from a spreadsheet thats been converted into a JSON file
def displayDataLoadMenu():
    print("[0] Load vocab JSON via default path")
    print("[1] Load vocab JSON via custom path")
    try:
        dataLoadID = int(input("Select [#] to execute: "))
    except:
        print("Invalid selection was made... try again")
        displayDataLoadMenu()

    filepath = default_data_path

    if(dataLoadID == 1):
        filepath = input("customDataPath: ")

    vocabData = utilities.GermanData()
    vocabData.load_vocabulary_dict(utilities.load_json_file(filepath))
    print(vocabData.get_random_flashcard())

    displayMainMenu()

def displayMainMenu():
    while True:
        utilities.print_seperator()
        print("[0] Play simple flashcards")
        print("[1] Play pick the correct one out of three")
        print("[8] Output specific card by index")
        print("[9] Output entire vocab file via ID")
        try:
            selectionID = input("Select [#] to execute: ")
        except:
            print("Invalid selection was made... try again")

        if(selectionID == "0"):
            print("Reworking")
        elif(selectionID == "1"):
            playFindTheCorrectOne()
        elif(selectionID == "8"):
            printIndividualVocabCard()
        elif(selectionID == "9"):
            printEntireVocabFile()
        elif(selectionID == "~"):
            print("You're already on the main menu")
            utilities.print_seperator()
        else:
            print("Invalid selection was made... try again")



def printIndividualVocabCard(vocabWords):
    vocabLength = (len(dict(vocabWords)))
    while True:
        try:
            utilities.print_seperator()
            choice = input(
                "Enter '~' to return or a value between 0-" + str(vocabLength) + ": ")
            # Return to main menu
            if (choice == "~"):
                return

            id = int(choice)
            printFlashCard(vocabWords[str(id)])
        except:
            print("Invalid data entry")

def playFindTheCorrectOne(vocabWords):
    print("TODO")
    utilities.print_seperator()

def printEntireVocabFile(vocabWords):
    print("TODO")

# ---------------------------------------------------------------------


# Run program
___init___()
