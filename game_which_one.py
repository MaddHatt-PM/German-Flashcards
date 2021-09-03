from utilities import *
import random

key__kategorie = "kategorie"
key__extra_card_count = "wrong_card_count"
all_categories = "all"

def config_options(germanData: GermanData):
    return

# give an english translation, presemt three german answers
def play_game(germanData:GermanData):
    print_seperator()
    game_options = { key__kategorie: all_categories, key__extra_card_count: 3 }
    correct_count = 0
    card_count = 0

    while True:
        # Card choosing and pruning
        chosen_card = germanData.get_random_flashcard(game_options.get(key__kategorie))
        answer = chosen_card.deutsch
        if ( germanData.get_kategorie_count(chosen_card) - 1 < game_options.get(key__extra_card_count)):
            print (chosen_card.deutsch, chosen_card.kategorie, germanData.get_kategorie_count(chosen_card))
            continue

        elif ( '{' in chosen_card.deutsch and '}' in chosen_card.deutsch):
            continue

        word_chooses = [chosen_card.deutsch]
        while len(word_chooses) < game_options.get(key__extra_card_count):
            possible_card = germanData.get_random_flashcard(chosen_card.kategorie)

            if ( '{' in possible_card.deutsch and '}' in possible_card.deutsch):
                continue
            if (possible_card.deutsch in word_chooses):
                continue

            index_pos = random.randrange(0, len(word_chooses))
            word_chooses.insert(index_pos , possible_card.deutsch)
            
        while True:
            print("Your word to translate is: " + chosen_card.englisch)
            print("Which word is the correct translation: ")
            for word in word_chooses:
                print("   - " + word)

            choice = input("\nEnter answer: ")

            if (choice == "/exit"):
                return

            if (choice == "/options"):
                game_options = config_options(germanData, game_options)
                continue

            if (choice.lower() == answer.lower()):
                print("Correct")
            else:
                print("Incorrect, the correct answer was: " + answer)
                if(input("Mark as correct anyways? Y or type the answer to advance: ") == 'Y'):
                    correct_count += 1

                card_count += 1
                print("Card's played: ", str(card_count), " Correct Responses: ", str(correct_count))