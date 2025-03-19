# print("Hello from lesson 9")
import turtle


# guess = input("What has to be broken before you can use it? =")
# isCorrect = False
# guess = guess.lower()
# guess = guess.split(" ")
# if "egg" in guess:
#     print("Great job! You got the answer correct! It’s clear that you understand the concept, and your reasoning is spot on. Keep up the excellent work—your attention to detail really paid off here. It's always rewarding to see your hard work come together. If you'd like to explore more or have any questions, feel free to ask. You're on the right track, and I’m confident you’ll continue to do well. Keep challenging yourself, and you’ll keep seeing great results. Well done once again!")
# else:
#     print("I appreciate your effort, but unfortunately, the answer you provided is incorrect. It seems like there might have been a small misunderstanding or mix-up in the details. No worries, though—mistakes happen to everyone! I’d be happy to help clarify things if you’d like to give it another try. Feel free to review the question or topic, and let me know if you'd like assistance or further explanation. I’m confident that with a bit more focus, you’ll be able to arrive at the correct answer. Keep up the great work, and don't hesitate to ask for help!")









window = turtle.Screen()
window.setup(width=600, height=600)
window.bgcolor("forestgreen")

t = turtle.Turtle()
t.shape("square")
t.up()
t.sety(250)
for i in range(-300, 301, 25):
    t.fillcolor("Black")
    t.setx(i)
    t.stamp()
for i in range(-250, 301, 25):
    t.fillcolor("White")
    t.setx(i)
    t.stamp()
    
















window.mainloop()




