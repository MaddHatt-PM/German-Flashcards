
import os
import time

class GermanData:
    def load_vocabulary_json():
        print("TODO")

    def load_statistics():
        print("TODO")

class flash_card:
    def __init__(self, gender:str, deutsch:str, englisch:str, kategorie:str):
        self.gender = gender
        self.deutsch = deutsch
        self.englisch = englisch
        self.kategorie = kategorie

    def print_card(self):
        print("Gender" + ": " + self.gender)
        print("Deutsch" + ": " + self.deutsch)
        print("Englisch" + ": " + self.englisch)
        print("Kategorie" + ": " + self.kategorie)


# ---------------------------------------------------------------------
# --- Helper Methods ---
# ----------------------
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


# def printFlashCard(flashcard):
#     if (len(str(flashcard[id_Gender])) != 0):
#         print(id_Gender + ": " + flashcard[id_Gender])
#     if (len(str(flashcard[id_Wort_Deutsch])) != 0):
#         print(id_Wort_Deutsch + ": " + flashcard[id_Wort_Deutsch])
#     if (len(str(flashcard[id_Englisch])) != 0):
#         print(id_Englisch + ": " + flashcard[id_Englisch])
#     if (len(str(flashcard[id_Kategorie])) != 0):
#         print(id_Kategorie + ": " + flashcard[id_Kategorie])