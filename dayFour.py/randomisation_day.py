import random
# Randomisation and Python Lists
# Nested list

#randint(a,b)
random_integer = random.randint(1,10)
print(random_integer)

#random float
random_float = random.random()
print(random_float)
#float takes [0,1)
#*5 for 0-5
random_float *5

#Love calculator
love_score = random.randint(1,100)
print(f"Your love score is {love_score}")

#Python Lists
vowels = ["a","e","i","o"]
print(vowels[1])
print(vowels[-1])
#edits the list
vowels[1] = "ee"
#adding an item to the end
vowels.append("u")
print(vowels)
num_of_vowel = len(vowels)
#last vowel
print(vowels[num_of_vowel-1])