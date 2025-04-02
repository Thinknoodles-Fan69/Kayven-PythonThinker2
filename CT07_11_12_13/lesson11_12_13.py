# print("Hello from lesson 11_12_13")
import random




# def diceGuess(guess):
#     winningNo = random.randint(1, 6)
#     if guess == winningNo:
#         print("You got the correct number ")
#     else:
#         print("Wah! you got it wrong!")


# diceGuess(input("Give me a number: "))












# tic tac toe
def initboard():
    board = []

    for i in range(3):
        row = []

        for a in range(3):
            row.append(" ")

        board.append(row)

    return board

def printboard(argboard):
    count = 1
    for row in argboard:

        for col in row:
            print(f"| {count} ", end="")

            if count % 3 == 0:
                print("|")
                print("-" * 13)
            count += 1


board = initboard()
printboard(board)

move = input("Enter a number from 1, 9: ")


if move.isdigit():
    pass
    if move >= 1 and move <= 9:
        pass
    else:
        print("Eh")
else:
    print("Eh! Siao Zabor ples pult a legit numble lerh. Isf u don then i cal polis and sgsecure.")

