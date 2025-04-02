# print("Hello from lesson 11_12_13")
import random


correct = False
def diceGuess(guess):
    winningNo = random.randint(1, 6)
    if guess == winningNo:
        correct = True
    else:
        correct = False

if correct == True:
    print("You got the correct number siao zabor")
else:
    print("Wah! ")
