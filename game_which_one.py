from utilities import *
import random

key__kategorie = "kategorie"
key__wrong_card_count = "wrong_card_count"
all_categories = "all"

def config_options(germanData: GermanData):
    return

# give an english translation, presemt three german answers
def play_game(germanData:GermanData):
    print_seperator()
    game_options = { key__kategorie: all_categories, key__wrong_card_count: 3 }
    correct_count = 0
    card_count = 0

    while True:

        # Card choosing and pruning
        chosen_card = germanData.get_random_flashcard(game_options.get(key__kategorie))
        if ( germanData.get_kategorie_count(chosen_card) - 1 < game_options.get(key__wrong_card_count)):
            continue

        elif ( '{' in chosen_card.deutsch and '}' in chosen_card.deutsch):
            continue

        word_chooses = [chosen_card.deutsch]
        while len(word_chooses) < game_options.get(key__wrong_card_count):
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

        return