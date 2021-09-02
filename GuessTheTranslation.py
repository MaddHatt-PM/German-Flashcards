from utilities import *

key__flip_rate = "flip_rate"
key__kategorie = "kategorie"
all_categories = "_all"

def config_options(game_options:dict):
    return game_options

def play_game(germanData:GermanData):
    game_options = { key__flip_rate: 0.5, key__kategorie:all_categories  }
    correct_count = 0
    card_count = 0
    
    print_seperator()
    print("Welcome to Guess the Translation!")
    print("type /exit at anytime to return to the main menu")
    print("type /options at anytime to change the kategorie or language flipping")
    
    while True:
        print_seperator()

        # Chosee card and setup variables
        chosenCard = germanData.get_random_flashcard(game_options.get(key__kategorie))
        question = chosenCard.gender + chosenCard.deutsch
        answer =  chosenCard.englisch

        flipLanguage = random.random() < game_options.get(key__flip_rate)
        answer_language = "English "
        if (flipLanguage):
            question, answer = answer, question
            answer_language = "Deutsch "

        print("Whats the " + answer_language + "translation of: " + question)
        choice = input("Enter answer: ")

        if (choice == "/exit"):
            return

        if (choice == "/options"):
            game_options = config_options(game_options)
            continue

        if (choice.lower() == answer.lower):
            print("Correct")
        else:
            print("Incorrect, the correct answer was: " + answer)
            if(input("Mark as correct anyways? Y or type the answer to advance: ") == 'Y'):
                correct_count += 1
        
        card_count += 1
        print("Card's played: ", str(card_count)," Correct Responses: ", str(correct_count))


    

