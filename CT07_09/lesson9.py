# print("Hello from lesson 9")

guess = input("What has to be broken before you can use it? =")
isCorrect = False
guess = guess.lower()
guess = guess.split(" ")
if "egg" in guess:
    print("Correct! Well done.")
else:
    print("I appreciate your effort, but unfortunately, the answer you provided is incorrect. It seems like there might have been a small misunderstanding or mix-up in the details. No worries, though—mistakes happen to everyone! I’d be happy to help clarify things if you’d like to give it another try. Feel free to review the question or topic, and let me know if you'd like assistance or further explanation. I’m confident that with a bit more focus, you’ll be able to arrive at the correct answer. Keep up the great work, and don't hesitate to ask for help!")