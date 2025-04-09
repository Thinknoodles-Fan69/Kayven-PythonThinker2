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

            if col == " ":
                print(f"| {count} ", end="")
            else:
                print(f"| {col} ", end="")

            if count % 3 == 0:
                print("|")
                print("-" * 13)
            count += 1


def get_player_move(argboard, playerNOW):
    while True:
        move = input(f"Player {playerNOW}, Ples enter a number from 1, 9: ")


        if move.isdigit():
            move = int(move)
            # pass
            if move >= 1 and move <= 9:
                move = move - 1
                row = move // 3
                col = move % 3
                print(f"row = {row}, col = {col}")


                if argboard[row][col] == " ":
                    argboard[row][col] = (playerNOW)
                    break
                else:
                    print(f"{move+1} is already taken. Choose another please")



                # pass
            else:
                print("Eh! Siao Dabor u butter pult an legit numble lerh. Isf u don then i suport adove hiter.")
        else:
            print("Eh! Siao Zabor ples pult a legit numble lerh. Isf u don then i cal polis and sgsecure.")
    return argboard


def getcurrentplayer(player):
    if player == "X":
        return "O"
    else:
        return "X"


def checkwin(argboard):
    win = [
        [argboard[0][0], argboard[0][1], argboard[0][2]],
        [argboard[1][0], argboard[1][1], argboard[1][2]],
        [argboard[2][0], argboard[2][1], argboard[2][2]],

        [argboard[0][0], argboard[1][0], argboard[2][0]],
        [argboard[0][1], argboard[1][1], argboard[2][1]],
        [argboard[0][2], argboard[1][2], argboard[2][2]],

        [argboard[0][0], argboard[1][1], argboard[2][2]],
        [argboard[0][2], argboard[1][1], argboard[2][0]]

    ]

    for condition in win:
        if condition[0] == condition[1] == condition[2] and condition[0] != " ":
            return True
    return False

def checktie(argboard):
    for row in argboard:
        for cell in row:
            if cell == " ":
                return False
    
    return True

board = initboard()
currentplayer = " "

while True:
    printboard(board)

    currentplayer = getcurrentplayer(currentplayer)

    board = get_player_move(board, currentplayer)

    if checkwin(board):
        print("*"*20)
        print(f"Player {currentplayer} wins!")
        printboard(board)
        break
    elif checktie(board):
        print("it is a tie. Say bye bye to lim beh")
        print()

        

    
