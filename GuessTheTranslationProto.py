import GermanFlashcards
# import HelperFunctions
import random

id_vocabWord = "vocabWords"
id_selectedKategorie = "kategorieCards"
id_selectedKategorieName = "kategorieName"
id_flipLanguageRate = "flipLanguageRate"


def ConfigureOptions(options: dict) -> dict:
    # options = {"vocabWords":options[0], "kategorieCards":options[1], "kategorieName":options[2], "flipLanguageRate":options[3]}
    languageFlipOptions = ("Deutsch Only", "Mixed", "Englisch Only",)
    languageFlipValues = (0, 0.5, 1,)

    while (True):
        GermanFlashcards.printSeperator()
        print("Game Options")
        print("[0] Selected Kategorie: " +
              options.get(id_selectedKategorieName))
        print("[1] Language Flip Option: " +
              languageFlipOptions[languageFlipValues.index(options[id_flipLanguageRate])])
        print("[2] Return to game")
        choice = input("Select [#] to execute: ")

        # Configure Kategorie
        if (choice == "0"):
            GermanFlashcards.printSeperator()

            # Get all kategory types
            unique_kategories = set()
            for entry in options[id_vocabWord]:
                unique_kategories.add(options[id_vocabWord][entry][GermanFlashcards.id_kategorie])

            if ("" in unique_kategories):
                unique_kategories.remove("")

            unique_kategories = list(unique_kategories)
            unique_kategories.append("All cards")
            index = 0
            for entry in unique_kategories:
                print('[' + str(index) + '] ' + unique_kategories[index])
                index += 1

            while True:
                try:
                    choice = int(input("Select [#] to choose category: "))
                    if (choice >= 0 and choice < index):
                        options[id_selectedKategorieName] = unique_kategories[choice]
                        selected = {}
                        for entry in options[id_vocabWord]:
                            if (options[id_vocabWord][entry][GermanFlashcards.id_kategorie] == options[id_selectedKategorieName]):
                                selected[entry] = options[id_vocabWord][entry]
                        options[id_selectedKategorie] = selected
                        break

                except TypeError:
                    print("Invalid data entry")

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
            return options
        else:
            print("Invalid input, please try again")


def PlayGame(vocabWord: dict):
    options = {"vocabWords": vocabWord, "kategorieCards": vocabWord,
               "kategorieName": "All Cards", "flipLanguageRate": 0.5}

    selectedKategorie = options[id_selectedKategorie]
    GermanFlashcards.printSeperator()
    print("Welcome to Guess the Translation!")
    print("type /exit at anytime to return to the main menu")
    print("type /options at anytime to change the kategorie or language flipping")

    vocabLength = (len(options[id_selectedKategorie]))
    cardCount = 0
    correctCount = 0
    offset = int(list(dict(options[id_selectedKategorie]).keys())[0])
    while True:
        GermanFlashcards.printSeperator()

        # Set up the flashcard for this turn
        # needs to either offset or sel
        chosenCard = (options[id_selectedKategorie])[str(random.randrange(0, vocabLength) + offset)]

        question = chosenCard[GermanFlashcards.key_wort_deutsch]
        answer = chosenCard[GermanFlashcards.id_englisch]

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
                gender = options[id_vocabWord][id][GermanFlashcards.key_gender]
                question = gender + " " + options[id_vocabWord][id][GermanFlashcards.key_wort_deutsch] + " " + question[end+1:]
                answer = (options[id_vocabWord][id])[GermanFlashcards.id_englisch] + " " + answer
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
            options = ConfigureOptions(options)
            selectedKategorie = options[id_selectedKategorie]
            vocabLength = (len(dict(selectedKategorie)))
            offset = list(dict(options[id_selectedKategorie]).keys())[0]
            print(vocabLength)
            continue

        if (choice.lower() == answer.lower()):
            print("Correct")
            correctCount += 1
        else:
            print("Incorrect, the correct answer was: " + answer)
            if(input("Mark as correct anyways? Y or type the answer to advance: ") == 'Y'):
                correctCount += 1
            # else:
            #     if (input)

        cardCount += 1
        print("Card's played: ", str(cardCount)," Correct Responses: ", str(correctCount))
