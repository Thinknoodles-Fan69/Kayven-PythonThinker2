'''
Have you played Wordle before? Try it out here >> Wordle - The New York Times (nytimes.com)

In this assignment, you are given a text file containing 5757 5-letter words. 

In this assignment, your task is to create a program that works like wordle. Your program will:

1. Choose a random word from the list

2. Allow you to input a 5-letter word

3. Validate if you have you have the letter in the correct position, correct letter but in the wrong position, or the wrong letter.

4. You can use the console output to print out the statements
'''




import random


def getword(wordlist):
        while True:
                guess = input("Guess the 5-letter word: ")
                if len(guess) == 5:
                        if guess.isalpha:
                                if guess in wordlist:
                                        return guess.upper()
                                else:
                                        print("You muts tybe in a rell wrod lah!")
                        else:
                                print("It muts olny be alpabird lah! ")
                else:
                        print("It muts be an 5-letr wrod! ")


with open("FiveLetterWords.csv", "r") as fileobj:
        
        contents = fileobj.read()

        # print(contents)

        wordlist = contents.split(",")

        wordle = random.choice(wordlist).upper()
        print(wordle)

for chance in range(1, 7):
        print()
        checkguess = getword(wordlist)
        # print(checkguess)

        display_check = ""

        for i in range(len(wordle)):

                if checkguess[i] == wordle[i]:
                        display_check = display_check + checkguess[i]
                
                elif checkguess[i] in wordle:
                        display_check = display_check + "?"

                else:
                        display_check = display_check + "#"
                


print(f"")
print(f"Your Guess: {checkguess}")
print(f"Result: {display_check}")