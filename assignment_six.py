# Thenea Sun
# Senior
# Oct. 23, 2018
# This program was a simulator of Squeal of Fortune, which let the user guess the secret words by guessing letter by
# letter in a limited number of times. It has relationship with our current studying unit.


import random


words = ["aberration", "abject", "accede", "acrimony", "adulation", "affinity", "aloof", "amicable", "antecedent",
         "antiquated", "arbitrary", "ascribe", "assuage", "austere", "behemoth", "benevolent", "buttress",
         "camaraderie", "caustic", "chide", "circumlocution", "cognizant", "commensurate", "compunction", "concoct",
         "connive", "contravene", "convoluted", "culpable", "debacle", "defunct", "denigrate", "derelict", "devious"
         , "discretion", "disparage", "divulge", "ebullient", "egregious", "emaciated", "emollient", "enmity"
         , "evanescent", "evince", "expiate", "fabricate", "fetter", "foil", "fortuitous", "goad", "harrowing",
         "harrowing", "hiatus", "imperative", "impervious", "inane", "incontrovertible", "indomitable"]


word = random.choice(words)
blank_list = []
# in order to make a blank list with "_" for the words


def starting():
    for x in range(len(word)):
        blank_list.append("_")
    print(blank_list)


def guess():
    number_guesses = 7
    for x in range(number_guesses):
        for x in range(len(word)):
            letter = input("Please guess a letter:")
            if letter == word[x]:
                print(letter, "is in the word!")
                blank_list[x] = letter
                print(blank_list)
            else:
                print("Sorry, but the letter is not in the word.")
                break
#


def main():
    while True:
        play = input("Would you like to start the game?")
        if play in ["y", "Y", "Yes", "yes", "Sure", "Why not", "Let's go", "Start", "start", "ya", "Yeah", "yeah",
                    "yay"]:
            print("Nice! Let's start the Squeal of Fortune now!")
            number_guesses = 7
            while number_guesses > 0 or "_" in word:
                starting()
                guess()
        else:
            print("Oh, I am feeling sad now, see you next time then!")
            break


main()

