# ----------------------------------
# German Flashcards by Patt Martin -
# ----------------------------------

"""
TODO:
Toggling off and on categories
"""

import os
import time
import json
import random

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


defaultDataPath = "C:\\Users\\Patri\\Desktop\\Code Projects\\German Flashcards\\Deutsch Vokabeln.json"
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
        print("[~] To return to the main menu at any time")
        try:
            selectionID = input("Select [#] to execute: ")
        except:
            print("Invalid selection was made... try again")

        if(selectionID == "0"):
            playSimpleFlashcards(vocabWords)
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


# Select a card at random
def playSimpleFlashcards(vocabWords):
    vocabLength = (len(dict(vocabWords)))
    cardCount = 0
    correctCount = 0
    while True:
        printSeperator()

        chosenCard = vocabWords[str(random.randrange(0, vocabLength))]
        germ0orEng1 = (int(random.random() * 100.0) % 1) == 0

        langQ = id_Wort_Deutsch
        langA = id_Englisch

        if (germ0orEng1 == False):
            langQ = id_Englisch
            langA = id_Wort_Deutsch

        print("Whats the translation of: " + chosenCard[langQ])
        choice = input("Whats the translation: ")

        if (choice == "~"):
            return

        if (choice == langA):
            print("Correct")
            correctCount += 1
        else:
            print("Incorrect, the correct answer was: " + chosenCard[langA])
            input("Mark as correct anyways? Y or N: ")

        cardCount += 1
        print("Card's played: ", str(cardCount),
              " Correct Responses: ", str(correctCount))


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
