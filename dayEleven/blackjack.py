import random
from blackjackart import blackjack_logo
blackjack_play=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if blackjack_play == "y":
    print(blackjack_logo)
else:
    print("You have exited from the blackjack")

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
#add function

x=[]
for n in range(0,2):
    random_cards = random.randint(0,len(cards)-1)
    random_user_cards = cards[random_cards]
    x.append(random_user_cards)
your_card = x
the_sum=sum(x)
print(f"Your cards: {your_card} , current score: {the_sum}")

if the_sum == 21:
    print("Blackjack! You won")
while the_sum<21:
    another_card=input("Type 'y' to get another card, type 'n' to pass: ")
    if another_card == "y":
        random_cards = random.randint(0,len(cards)-1)
        random_user_cards = cards[random_cards]
        x.append(random_user_cards)
        your_card = x
        the_sum = sum(x)
        print(f"Your cards: {your_card} , current score: {the_sum}")
    
    else:
        the_sum>21
        print(f"Your final hand is {your_card}, current scare {the_sum}")

    
else:
    print("You lose")

