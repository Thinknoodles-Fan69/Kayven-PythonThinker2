# print("Hello from lesson 11_12_13")
import random




def diceGuess(guess):
    correct = False
    winningNo = random.randint(1, 6)
    if guess == winningNo:
        correct = True
    else:
        correct = False

diceGuess()
if correct == True:
    print("You got the correct number ")
else:
    print("Wah! you got it wrong!")
