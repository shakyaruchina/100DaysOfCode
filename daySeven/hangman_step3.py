#negation
import random

word_list = ["aardvark","baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing
print(f'The random word is {chosen_word}')

#an empty list
display =[]
for letter in range(len(chosen_word)):
    #adding "_" for each letter in the chosen word to guess
    display.append("_")

#while loop to guess again and again until evth is guessed

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

#check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win")
