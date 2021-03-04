#! /usr/bin/env python

import random

# from hangman_words import word_list
import hangman_words
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
#number of lives in the game
lives = 6

from hangman_art import logo, stages
print(logo)
#testing
print(f'The random word is {chosen_word}')

#an empty list
display =[]
for letter in range(word_length):
    #adding "_" for each letter in the chosen word to guess
    display.append("_")

#while loop to guess again and again until evth is guessed

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed the letter {guess}")

#check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #resucing lives when guessed wrong letter
    #when lives= 0 ; You lose

    if guess not in chosen_word:
        print(f"You guessed {guess}, that is not in the word. You lose a life")
        lives -=1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word is {chosen_word}")

    #join all the elements in the list and turn it into a string
    print(f"{' '.join(display)}")

    #check if user has got all letters.

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
    