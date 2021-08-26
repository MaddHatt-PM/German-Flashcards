import GermanFlashcards
import random

def PlayGame(vocabWords):
    vocabLength = (len(dict(vocabWords)))
    cardCount = 0
    correctCount = 0
    while True:
        GermanFlashcards.printSeperator()

        chosenCard = vocabWords[str(random.randrange(0, vocabLength))]
        germ0orEng1 = (int(random.random() * 100.0) % 1) == 0

        langQ = GermanFlashcards.id_Wort_Deutsch
        langA = GermanFlashcards.id_Englisch

        if (germ0orEng1 == False):
            langQ = GermanFlashcards.id_Englisch
            langA = GermanFlashcards.id_Wort_Deutsch

        print("Whats the translation of: " + chosenCard[langQ])
        choice = input("Whats the translation: ")

        if (choice == "~"):
            return

        if (choice == langA):
            print("Correct")
            correctCount += 1
        else:
            print("Incorrect, the correct answer was: " + chosenCard[langA])
            if(input("Mark as correct anyways? Y or N: ") == 'Y'):
                correctCount += 1

        cardCount += 1
        print("Card's played: ", str(cardCount),
              " Correct Responses: ", str(correctCount))