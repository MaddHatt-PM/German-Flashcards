# ----------------------------------
# German Flashcards by Patt Martin -
# ----------------------------------

import os
import time
import json
import random
import GuessTheTranslation
import HelperFunctions

# Starter method


def ___init___():
    clearConsole()
    displayDataLoadMenu()


# ---------------------------------------------------------------------
# --- Helper Methods ---
# ----------------------
def clearConsole():
    os.system("cls")


def animateLoadingText(text):
    print(text, sep="", end="")
    time.sleep(0.2)
    print('.', sep="", end="")
    time.sleep(0.2)
    print('.', sep="", end="")
    time.sleep(0.2)
    print('.', sep="")
    time.sleep(0.4)


def printSeperator():
    print("\n---------------------------------------------------------------------\n")


def printFlashCard(flashcard):
    if (len(str(flashcard[id_Gender])) != 0):
        print(id_Gender + ": " + flashcard[id_Gender])
    if (len(str(flashcard[id_Wort_Deutsch])) != 0):
        print(id_Wort_Deutsch + ": " + flashcard[id_Wort_Deutsch])
    if (len(str(flashcard[id_Englisch])) != 0):
        print(id_Englisch + ": " + flashcard[id_Englisch])
    if (len(str(flashcard[id_Kategorie])) != 0):
        print(id_Kategorie + ": " + flashcard[id_Kategorie])


# ---------------------------------------------------------------------
# --- Main Methods ---
# --------------------

defaultDataPath = "Deutsch Vokabeln.json"
# Identifier variables from my spreadsheet, custom ones aren't going to work
id_Gender = "Gender"
id_Wort_Deutsch = "Wort Deutsch"
id_Englisch = "Englisch"
id_Kategorie = "Kategorie"


# Get the vocabulary words from a spreadsheet thats been converted into a JSON file
def displayDataLoadMenu():
    print("[0] Load vocab JSON via default path")
    print("[1] Load vocab JSON via custom path")
    try:
        dataLoadID = int(input("Select [#] to execute: "))
    except:
        print("Invalid selection was made... try again")
        displayDataLoadMenu()

    filepath = defaultDataPath

    if(dataLoadID == 1):
        filepath = input("customDataPath: ")
        filepath = str.replace(filepath, "\\", "\\\\")

    # Load the file path as a file then convert it to readable bytes for json.load to use
    animateLoadingText("Loading")
    with open(filepath, encoding="utf8") as jsonFileData:
        vocabWords = json.load(jsonFileData)

    vocabLength = len(vocabWords)
    print(str(vocabLength) + " vocabulary cards loaded")

    displayMainMenu(vocabWords)

def displayMainMenu(vocabWords):
    while True:
        printSeperator()
        print("[0] Play simple flashcards")
        print("[1] Play pick the correct one out of three")
        print("[8] Output specific card by index")
        print("[9] Output entire vocab file via ID")
        try:
            selectionID = input("Select [#] to execute: ")
        except:
            print("Invalid selection was made... try again")

        if(selectionID == "0"):
            GuessTheTranslation.PlayGame(vocabWords)
        elif(selectionID == "1"):
            playFindTheCorrectOne(vocabWords)
        elif(selectionID == "8"):
            printIndividualVocabCard(vocabWords)
        elif(selectionID == "9"):
            printEntireVocabFile(vocabWords)
        elif(selectionID == "~"):
            print("You're already on the main menu")
            printSeperator()
        else:
            print("Invalid selection was made... try again")

def playFindTheCorrectOne(vocabWords):
    print("TODO")
    printSeperator()


def printIndividualVocabCard(vocabWords):
    vocabLength = (len(dict(vocabWords)))
    while True:
        try:
            printSeperator()
            choice = input(
                "Enter '~' to return or a value between 0-" + str(vocabLength) + ": ")
            # Return to main menu
            if (choice == "~"):
                return

            id = int(choice)
            printFlashCard(vocabWords[str(id)])
        except:
            print("Invalid data entry")


def printEntireVocabFile(vocabWords):
    print("TODO")

# ---------------------------------------------------------------------


# Run program
___init___()
