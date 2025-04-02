# print("Hello from lesson 11_12_13")
import random




def diceGuess(guess):
    guess = False
    winningNo = random.randint(1, 6)
    if guess == winningNo:
        print("You got the correct number ")
    else:
        correct = False


if diceGuess(input("Give me a number: ")):
    print("You got the correct number ")
else:
    print("Wah! you got it wrong!")
