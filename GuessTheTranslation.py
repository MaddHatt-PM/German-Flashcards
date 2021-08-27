import GermanFlashcards
import HelperFunctions
import random

gameOptions = {"vocabWords":{}, "kategorieCards":{}, "kategorieName":str, "flipLanguageRate":float}

id_vocabWord = "vocabWords"
id_selectedKategorie = "kategorieCards"
id_selectedKategorieName = "kategorieName"
id_flipLanguageRate = "flipLanguageRate"

def ConfigureOptions(options:dict):
    # options = {"vocabWords":options[0], "kategorieCards":options[1], "kategorieName":options[2], "flipLanguageRate":options[3]}
    languageFlipOptions = ("Deutsch Only", "Mixed", "Englisch Only",)
    languageFlipValues = (0, 0.5, 1,)

    while (True):
        GermanFlashcards.printSeperator()
        print("Game Options")
        print("[0] Selected Kategorie: " + options.get(id_selectedKategorieName))
        print("[1] Language Flip Option: " + languageFlipOptions[languageFlipValues.index(options[id_flipLanguageRate])] )
        print("[2] Return to game")
        choice = input("Select [#] to execute: ")

        # Configure Kategorie
        if (choice == "0"):
            print("TODO")
        
        # Configure Language Flip Options
        elif(choice == "1"):
            while(True):
                GermanFlashcards.printSeperator()
                print("[0]", languageFlipOptions[0])
                print("[1]", languageFlipOptions[1])
                print("[2]", languageFlipOptions[2])
                choice = input("Select language flip type: ")
                if(choice == "0" or choice == "1" or choice == "2"):
                    options[id_flipLanguageRate] = languageFlipValues[int(choice)]
                    print("Language flip type saved")
                    break
                else:
                    print("Invalid data entry")


        # Exit the options menu
        elif(choice == "2"):
            return
        else:
            print ("Invalid input, please try again")



def PlayGame(vocabWord: dict):
    options = {"vocabWords":vocabWord,"kategorieCards":vocabWord.copy, "kategorieName":"All Cards", "flipLanguageRate":0.5}

    selectedKategorie = vocabWord
    GermanFlashcards.printSeperator()
    print ("Welcome to Guess the Translation!")
    print("type /exit at anytime to return to the main menu")
    print("type /options at anytime to change the kategorie or language flipping")

    vocabLength = (len(dict(selectedKategorie)))
    cardCount = 0
    correctCount = 0
    while True:
        GermanFlashcards.printSeperator()

        # Set up the flashcard for this turn
        chosenCard = selectedKategorie[str(random.randrange(0, vocabLength))]
        question = chosenCard[GermanFlashcards.id_Wort_Deutsch]
        answer = chosenCard[GermanFlashcards.id_Englisch]

        # {-} Indicates that chosenWord contains references to another vocabWord to be replaced
        if('{' in question and '}' in question):

            # isolate options substring
            start = question.find('{')
            end = question.find('}')
            addOptions = question[start+1:end]

            # Create an options tuple and add an impossible to have the plain version be selectable
            addOptions += ", -1"
            addOptions = tuple(eval(addOptions))
            id = str(addOptions[(random.randrange(0, len(addOptions)))])
            if (id != "-1"):
                question = selectedKategorie[id][GermanFlashcards.id_Wort_Deutsch] + " " + question[end+1:]
                answer = (selectedKategorie[id])[
                    GermanFlashcards.id_Englisch] + " " + answer
                question = question.replace("...", "")
                answer = answer.replace("...", "")
            else:
                question = question[end+1:]

        flipLanguage = random.random() < options[id_flipLanguageRate]
        if (flipLanguage):
            question, answer = answer, question

        print("Whats the translation of: " + question)
        choice = input("Whats the translation: ")

        if (choice == "/exit"):
            return
        
        if (choice == "/options"):
            ConfigureOptions(options)
            continue

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
