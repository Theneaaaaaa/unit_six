# Thenea Sun
# Senior
# Oct. 23, 2018
# This program was a simulator of Squeal of Fortune, which let the user guess the secret words by guessing letter by
# letter in a limited number of times. It has relationship with our current studying unit.


import random


def main():
    words = ["aberration", "abject", "ability", "able", "about", "above", "accept", "according", "account", "across",
             "act", "action", "activity", "actually", "add", "address", "administration", "admit", "adult", "affect",
             "after", "again", "against", "age", "agency", "agent", "ago", "agree", "agreement", "ahead", "air", "all",]
    # all those words are starting with "a".
    word = random.choice(words)
    blank_list = []
    number_guesses = 7
    number_guessed = 0
    # in order to make a blank list with "_" for the words
    while True:
        play = input("Would you like to start the game?")
        if play in ["y", "Y", "Yes", "yes", "Sure", "Why not", "Let's go", "Start", "start", "ya", "Yeah", "yeah",
                    "yay"]:
            print("Nice! Let's start the Squeal of Fortune now!")
            for x in range(len(word)):
                    blank_list.append("_")
            while number_guesses > 0 and "_" in blank_list:
                print(blank_list)
                letter = input("Please guess a letter:")
                if letter in word:
                    for x in range(len(word)):
                        if letter == word[x]:
                            blank_list[x] = letter
    # This is one of the most important function in this code. It helps with correcting the guesses
                else:
                    print("Sorry, but the letter is not in the word.")
                    number_guessed = number_guessed + 1
                    if number_guessed >= 7:
                        print("You had used all your chances, sorry, you lost.")
                        break
                while "_" not in blank_list:
                    print("Congratulation! You got the word!")
                    break
        else:
            print("Oh, that's sad, see you next time then!")
            break


main()

