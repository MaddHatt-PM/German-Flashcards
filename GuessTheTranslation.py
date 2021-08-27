import GermanFlashcards
import HelperFunctions
import random


def PlayGame(vocabWords:dict):
    vocabLength = (len(dict(vocabWords)))
    cardCount = 0
    correctCount = 0
    flipLanguageRate = 0.5
    while True:
        GermanFlashcards.printSeperator()

        # Set up the flashcard for this turn
        chosenCard = vocabWords[str(random.randrange(0, vocabLength))]
        question = chosenCard[GermanFlashcards.id_Wort_Deutsch]
        answer = chosenCard[GermanFlashcards.id_Englisch]

        # {-} Indicates that chosenWord contains references to another vocabWord to be replaced
        if('{' in question and '}' in question):

            # isolate options substring
            start = question.find('{')
            end = question.find('}')
            options = question[start+1:end]

            # Create an options tuple and add an impossible to have the plain version be selectable
            options += ", -1"
            options = tuple(eval(options))
            id = str(options[(random.randrange(0, len(options)))])
            if (id != "-1"):
                question = vocabWords[id][GermanFlashcards.id_Wort_Deutsch] + " " + question[end+1:]
                answer = (vocabWords[id])[GermanFlashcards.id_Englisch] + " " + answer
                question = question.replace("...", "")
                answer = answer.replace("...", "")
            else:
                question = question[end+1:]
                

        flipLanguage = random.random() < flipLanguageRate
        if (flipLanguage):
            question, answer = answer, question


        print("Whats the translation of: " + question)
        choice = input("Whats the translation: ")

        if (choice == "~"):
            return


        if (choice.lower() == answer.lower()):
            print("Correct")
            correctCount += 1
        else:
            print("Incorrect, the correct answer was: " + answer)
            if(input("Mark as correct anyways? Y or N: ") == 'Y'):
                correctCount += 1

        cardCount += 1
        print("Card's played: ", str(cardCount),
              " Correct Responses: ", str(correctCount))