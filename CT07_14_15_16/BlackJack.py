import random
import time
suits = ["♣ CLUB", "♦ DIAMOND","❤ HEART","♠ SPADE"]
ranks = ['2','3','4','5','6','7','8','9','JACK','QUEEN','KING','ACE']


values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
'JACK':10, 'QUEEN':10,'KING':10, 'ACE':11}

# Store Variable
deck = []
player_hand = []
banker_hand = []

# To build the deck
for suit in suits:
    for rank in ranks:
        deck.append([rank, suit])

# Shuffle the deck
for i in range(10):
    random.shuffle(deck)


print("\n\n", "*" * 30)
print("{:^30}".format("Python Black Jack"))
print("*" * 30, "\n\n")


# print(deck)

# Draw out the card
card1 = deck.pop()

# Draw out 2 cards
player_hand = [deck.pop(), deck.pop()]
banker_hand = [deck.pop(), deck.pop()]

def calculate(hand):
    points = 0
    count_aces = 0

    for card in hand:
        cardpoint = values[card[0]]
        points += cardpoint

        if card[1] == "ACE":
            count_aces += 1 #count how many aces you have

    while points > 21 and count_aces > 0:
        points -= 10
        count_aces -= 1
    
    return points

# function to display hand
print()
# params: hand, typeofhand (banker_hide, player_show, banker_show)
def show_hand(hand, playtype):
    if playtype == "player_show":
        print("% " * 15)
        print("{:^30}".format("PLAYER HAND"))
        print()
        for card in hand:
            print("{:^30}".format(f"{card[0]} {card[1]}"))
        print()
        print("{:^30}".format(f"You have {calculate(hand)} points"))
        print("% " * 15)
        print("")

    elif playtype == "banker_hide":
        print("$ " * 15)
        print("{:^30}".format("DEALER HAND"))
        print()
        print("{:^30}".format(f"{hand[0][0]}{hand[0][1]}"))
        print("{:^30}".format("? ? ? " * 3))
        print("$ " * 15)
        print()

    elif playtype == "banker_show":
        print("% " * 15)
        print("{:^30}".format("DEALER SHOW HAND"))
        print()
        for card in hand:
            print("{:^30}".format(f"{card[0]} {card[1]}"))
        print()
        print("{:^30}".format(f"Dealer have {calculate(hand)} points"))
        print("% " * 15)
        print("")

    print()

# print(player_hand)
# print(banker_hand)

while True:
    show_hand(banker_hand, "banker_hide")
    show_hand(player_hand, "player_show")
    

    if calculate(player_hand) == 21:
        print("You win! Black Jack!")
        break
    else:
        action = input("1 = hit, 2 = check :")
        if action == "1":
            player_hand.append(deck.pop())
            show_hand(player_hand, "player_show")

            if calculate(player_hand) > 21:
                print("You busted! Too bad!")
                break
        elif action == "2":
            

            while calculate(banker_hand) <= 17:
                print(">>>Banker is thinking<<<..")
                time.sleep(random.randint(1, 2))
                banker_hand.append(deck.pop())
                show_hand(banker_hand, "banker_show")
            
            if calculate(banker_hand) > 21:
                print("Dealer busted!")
                show_hand(banker_hand, "banker_show")
                break
            else:
                # check winning condition
                player_point = calculate(player_hand)
                banker_point = calculate(banker_hand)

                if player_point > banker_point:
                    print("Player Wins!")
                else:
                    print("Dealer Wins!")

                break
