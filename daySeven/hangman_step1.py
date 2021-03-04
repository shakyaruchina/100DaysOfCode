#problem that only prints if the user guessed letter(1) is in the chosen random word or not.
import random
#list
word_list =["aardvark", "baboon", "camel"]
#randomisation
chosen_word = random.choice(word_list)
#lowecase
guess = input("Guess a letter:").lower()

#for loop inside chosen_word
for letter in chosen_word:
    #if/else condition
    if letter == guess:
        print("You got the letter right!")
    else:
        print("You got it wrong,try again")
