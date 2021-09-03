from utilities import *
import time
import random

key__number_min = "min"
key__number_max = "max"

def config_options(germanData:GermanData, game_options:dict):
    return

def play_game(germanData:GermanData):
    game_options = {key__number_min: 0, key__number_max:60}
    correct_count = 0
    card_count = 0

    while True:
        # print_seperator()
        
        selectedNumber = random.randint(game_options.get(key__number_min), game_options.get(key__number_max))
        answer = int_to_deutsch(selectedNumber)
        print(answer)
        time.sleep(0.5)
