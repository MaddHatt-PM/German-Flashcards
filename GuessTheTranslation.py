from utilities import *

key__kategorie = "kategorie"
all_categories = "all"
key__flip_rate = "flip_rate"
flip_language_rates = (0, 0.5, 1,)

def config_options(germanData:GermanData , game_options:dict):
    languageFlipOptions = ("Deutsch Only", "Mixed", "Englisch Only",)

    while (True):
        print_seperator()
        print("Game Options")
        print("[0] Selected Kategorie: " + game_options.get(key__kategorie))
        print("[1] Language Flip Option: " + languageFlipOptions[game_options[key__flip_rate]])
        print("[2] Return to game")
        choice = input("Select [#] to execute: ")

        # Configure Kategorie
        if (choice == "0"):
            print_seperator()

            kategories = germanData.kategories.copy()
            kategories.append("All cards")

            index = 0
            for entry in kategories:
                print('[' + str(index) + '] ' + kategories[index])
                index += 1

            while True:
                try:
                    choice = int(input("Select [#] to choose category: "))
                    if (choice >= 0 and choice < index):
                        game_options[key__kategorie] = kategories[choice]
                        break

                except TypeError:
                    print("Invalid data entry")

        # Configure Language Flip Options
        elif(choice == "1"):
            while(True):
                print_seperator()
                print("[0]", languageFlipOptions[0])
                print("[1]", languageFlipOptions[1])
                print("[2]", languageFlipOptions[2])
                choice = input("Select language flip type: ")
                if(choice == "0" or choice == "1" or choice == "2"):
                    game_options[key__flip_rate] = flip_language_rates[int(choice)]
                    print("Language flip type saved")
                    break
                else:
                    print("Invalid data entry")

        # Exit the options menu
        elif(choice == "2"):
            return game_options
        else:
            print("Invalid input, please try again")

def play_game(germanData:GermanData):
    game_options = { key__flip_rate: 1, key__kategorie:all_categories  }
    correct_count = 0
    card_count = 0
    
    print_seperator()
    print("Welcome to Guess the Translation!")
    print("type /exit at anytime to return to the main menu")
    print("type /options at anytime to change the kategorie or language flipping")
    
    while True:
        print_seperator()

        # Choose card and setup variables
        chosenCard = germanData.get_random_flashcard(game_options.get(key__kategorie))
        question = chosenCard.gender + chosenCard.deutsch
        answer =  chosenCard.englisch

        # {-} Indicates that chosenWord contains references to another vocabWord to be replaced
        if('{' in question and '}' in question):

            output = germanData.combine_flashcards(chosenCard, question, answer)
            question = output[0]
            answer = output[1]

            # isolate options substring
            start = question.find('{')
            end = question.find('}')
            addOptions = question[start+1:end]

            # Create an options tuple and add an impossible to have the plain version be selectable
            addOptions += ", -1"
            addOptions = tuple(eval(addOptions))
            id = str(addOptions[(random.randrange(0, len(addOptions)))])
            if (id != "-1"):
                add_card = germanData.get_flashcard(id)

                question = add_card.gender + " " + add_card.deutsch + " " + chosenCard.deutsch[end+1:] 
                answer = add_card.englisch + " " + chosenCard.englisch
                question = question.replace("...", "")
                answer = answer.replace("...", "")
            else:
                question = question[end+1:]

        question = chosenCard.gender + " " + question
        flip_language = flip_language_rates[random.random() < game_options.get(key__flip_rate)]
        answer_language = "English "
        if flip_language:
            question, answer = answer, question
            answer_language = "Deutsch "

        print("Whats the " + answer_language + "translation of: " + question)
        choice = input("Enter answer: ")

        if (choice == "/exit"):
            return

        if (choice == "/options"):
            game_options = config_options(germanData, game_options)
            continue

        if (choice.lower() == answer.lower):
            print("Correct")
        else:
            print("Incorrect, the correct answer was: " + answer)
            if(input("Mark as correct anyways? Y or type the answer to advance: ") == 'Y'):
                correct_count += 1
        
        card_count += 1
        print("Card's played: ", str(card_count)," Correct Responses: ", str(correct_count))