import os
import time
import json
import random


class flash_card:
    def __init__(self, gender: str, deutsch: str, englisch: str, kategorie: str):
        self.gender = gender
        self.deutsch = deutsch
        self.englisch = englisch
        self.kategorie = kategorie

    def print_card(self):
        print("Gender" + ": " + self.gender)
        print("Deutsch" + ": " + self.deutsch)
        print("Englisch" + ": " + self.englisch)
        print("Kategorie" + ": " + self.kategorie)

    
    def __repr__(self) -> str:
        return self.deutsch

    def __str__(self):
        return self.deutsch


class GermanData:
    def __init__(self):
        self.kategories = []
        self.vocab_words = []


    def load_vocabulary_dict(self, input: dict):
        # Dictionary keys straight from the spreadsheet/json
        key_gender = "Gender"
        key_wort_deutsch = "Wort Deutsch"
        key_englisch = "Englisch"
        key_kategorie = "Kategorie"

        for key_id in input:
            card = flash_card(
                input[key_id][key_gender],
                input[key_id][key_wort_deutsch],
                input[key_id][key_englisch],
                input[key_id][key_kategorie])

            self.vocab_words.append(card)

            if(input[key_id][key_kategorie] in self.kategories == False):
                self.kategories.append(key_id[key_kategorie])

    def load_statistics():
        print("TODO")

    def load_conjugations(self, input:dict):
        print("TODO")

    def get_flashcard(self, id:int) -> flash_card:
        return self.vocab_words[id]

    def get_random_flashcard(self, kategorie = "all") -> flash_card:
        while True:
            chosen_flashcard = self.vocab_words[random.randrange(0, len(self.vocab_words))]
            if(kategorie == "all" or chosen_flashcard.kategorie == kategorie):
                return chosen_flashcard

    def get_kategorie_count(self, kategorie:str):
        counter = 0
        for flashcard in self.vocab_words:
            if (flashcard.kategorie == kategorie):
                counter += 1
        return counter

    def combine_flashcards(self, chosenCard:flash_card , question:str, answer:str) -> tuple:
        # isolate options substring
        start = question.find('{')
        end = question.find('}')
        addOptions = question[start+1:end]

        # Create an options tuple and add an impossible to have the plain version be selectable
        addOptions += ", -1"
        addOptions = tuple(eval(addOptions))
        id = str(addOptions[(random.randrange(0, len(addOptions)))])
        if (id != "-1"):
            add_card = self.get_flashcard(id)

            question = add_card.gender + " " + add_card.deutsch + " " + chosenCard.deutsch[end+1:] 
            answer = add_card.englisch + " " + chosenCard.englisch
            question = question.replace("...", "")
            answer = answer.replace("...", "")
        else:
            question = question[end+1:]

        return tuple(question, answer)

# ---------------------------------------------------------------------
# --- Helper Methods ---
# ----------------------
def load_json_file(filepath):
    filepath = str.replace(filepath, "\\", "\\\\")
    with open(filepath, encoding="utf8") as jsonFileData:
        output = json.load(jsonFileData)

    return output


def clear_console():
    os.system("cls")


def show_loading_text(text):
    print(text, sep="", end="")
    time.sleep(0.2)
    print('.', sep="", end="")
    time.sleep(0.2)
    print('.', sep="", end="")
    time.sleep(0.2)
    print('.', sep="")
    time.sleep(0.4)


def print_seperator():
    print("\n---------------------------------------------------------------------\n")
