import random
from time import sleep

def deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

print("Blackjack!")

if input("Do you want to play? (y/n) ") == "n":
    exit()

dealer_total = 0
player_total = 0
player_stand_flag = False
dealer_stand_flag = False

# Deal cards
for i in range(0, 2):
    dealer_total += deal()
    player_total += deal()

print(f"\nYou: {player_total}\nDealer: {dealer_total}")

# Display option to hit or stand

while player_total < 21 and player_stand_flag is False:

    hit_or_stand = input("\nHit or stand? (h/s) ")

    if hit_or_stand == "h":
        player_total += deal()
        print(f"\nYou: {player_total}")
    elif hit_or_stand == "s":
        player_stand_flag = True
    else:
        print("Try again")

if player_total > 21:
    print(f"\nYou: {player_total}\nDealer: {dealer_total}")
    print(f"The house won")
    exit()


while dealer_total < 21 and dealer_stand_flag is False:
    # if dealer_total is between 15 and 20, 1 in 3 chance of choosing to hit
    if 20 >= dealer_total > 15:
        if random.randint(0, 2) == 1:
            dealer_total += deal()
            print(f"\nDealer: {dealer_total}")
        else:
            dealer_stand_flag = True
            print("Dealer stands")
    # if dealer_total is between 10 and 14, 1 in 2 chance of choosing to hit
    elif 15 >= dealer_total > 10:
        if random.randint(0, 1):
            dealer_total += deal()
            print(f"\nDealer: {dealer_total}")
        else:
            dealer_stand_flag = True
            print("Dealer stands")
    elif dealer_total <= 10:
        dealer_total += deal()
        print(f"\nDealer: {dealer_total}")

    sleep(2)

if dealer_total > 21:
    print(f"\nYou: {player_total}\nDealer: {dealer_total}")
    print("You won!")
    exit()

if player_total == dealer_total:
    print("Push!")
    exit()

if player_total == 21:
    print("You won!")

if dealer_total == 21:
    print("The house won")

if dealer_total < 21 and player_total < 21:
    if dealer_total > player_total:
        print(f"\nYou: {player_total}\nDealer: {dealer_total}")
        print(f"The house won")
    elif dealer_total < player_total:
        print(f"\nYou: {player_total}\nDealer: {dealer_total}")
        print(f"You won!")
