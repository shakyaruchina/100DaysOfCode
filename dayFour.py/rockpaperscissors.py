import random

#ASCII
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#List 
#game_images= [rock,paper,scissors]

#user input
#rps:rock paper scissor game
rps=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

#print(game_images[rps]

if rps == 0:
  print(rock)
elif rps == 1:
  print(paper)
elif rps==2:
  print(scissors) 
else:
  print("You typed an invalid number. You lose")

#Computer random generator
print("Computer chose: ")
computer_random = random.randint(0,2)

#alternate way
#if rps>=3 or rps<3:
#print("You typed an invalid number. You lose")
#else:
#print(game_images[computer_random]

if computer_random == 0:
  print(rock)
elif computer_random == 1:
  print(paper)
else:
  print(scissors)


#Results
#if condition
#and operator
if rps == computer_random:
  print("Its a draw")
elif rps== 0 and computer_random == 1:
  print("You Lose")
elif rps== 0 and computer_random == 2:
  print("You Win") 
elif rps== 1 and computer_random == 0:
  print("You Win")
elif rps== 1 and computer_random == 2:
  print("You Lose")
elif rps== 2 and computer_random == 0:
  print("You Win")
elif rps== 2 and computer_random == 1:
  print("You Win")
else:
  print("You typed an invalid number. You lose") 