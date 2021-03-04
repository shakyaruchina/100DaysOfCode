import random

word_list =["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#for test
print(f'The solution is {chosen_word}.')

#an empty list
display =[]
for letter in range(len(chosen_word)):
    #adding "_" for each letter in the chosen word to guess
    display.append("_")

guess = input("Guess a letter:").lower()

#replacing "_" when right letter is guessed.
for position in range(len(chosen_word)):
    if chosen_word[position] == guess:
        display[position] = chosen_word[position]
print(display)
