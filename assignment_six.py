# Thenea Sun
# Senior
# Oct. 23, 2018
# This program was a simulator of Squeal of Fortune, which let the user guess the secret words by guessing letter by
# letter in a limited number of times. It has relationship with our current studying unit.


import random()

while True:
    play = input("Would you like to start the game?")
    if play in ["y", "Y", "Yes", "yes", "Sure", "Why not", "Let's go", "Start", "start", "ya", "Yeah", "yeah", "yay"]:
        print("Nice! Let's start the Squeal of Fortune now!")
        break
    else:
        print("Oh, I am feeling sad now, see you next time then!")
        break


words = ["aberration", "abject", "accede", "acrimony", "adulation", "affinity", "aloof", "amicable", "antecedent",
             "antiquated", "arbitrary", "ascribe", "assuage", "austere", "behemoth", "benevolent", "buttress",
             "camaraderie", "caustic", "chide", "circumlocution", "cognizant", "commensurate", "compunction", "concoct",
             "connive", "contravene", "convoluted", "culpable", "debacle", "defunct", "denigrate", "derelict", "devious"
             , "discretion", "disparage", "divulge", "ebullient", "egregious", "emaciated", "emollient", "enmity"
             , "evanescent", "evince", "expiate", "fabricate", "fetter", "foil", "fortuitous", "goad", "harrowing",
             "harrowing", "hiatus", "imperative", "impervious", "inane", "incontrovertible", "indomitable"]


def choose_word():
    random.choice(words)
    return words

def fill_blanks():
    blank_list = []
    for x in range(len(choose_word())):
        