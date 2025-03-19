# print("Hello from lesson 9")

guess = [input("What has to be broken before you can use it? =")]
isCorrect = False
guess = guess.lower()
guess = guess.split(" ")
for i in guess:
    if "egg" in guess:
        isCorrect = True
if isCorrect == True:
    print("Correct! Well done.")
else:
    print("")