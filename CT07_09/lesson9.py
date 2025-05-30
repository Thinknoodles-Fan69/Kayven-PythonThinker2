# print("Hello from lesson 9")
import turtle
import random

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
t.seth(0)
for i in range(-300, 301, 50):
    t.fillcolor("Black")
    t.setx(i)
    t.stamp()
    t.fillcolor("White")
    t.setx(i + 25)
    t.stamp()


t.goto(-300, -250)
t.seth(0)
t.pencolor("white")
t.pendown()
t.forward(600)
t.hideturtle

Kayla = turtle.Turtle()
Kayla.penup()
Kayla.seth(90)
Kayla.shape("turtle")
Kayla.color("red")
Kayla.goto(0, -250)
Kayla.write("Kayla", align="center", font=("Arial", 20))


Isabella = turtle.Turtle()
Isabella.penup()
Isabella.seth(90)
Isabella.shape("turtle")
Isabella.color("White")
Isabella.goto(150, -250)
Isabella.write("Isabella", align="center", font=("Arial", 20))


Nat = turtle.Turtle()
Nat.penup()
Nat.seth(90)
Nat.shape("turtle")
Nat.color("Yellow")
Nat.goto(-150, -250)
Nat.write("Nat", align="center", font=("Arial", 20))

guess = input("Who do you think will win this long and tiring race which includes loads of obstacles and challenges in this competition called The Tortoise Challenge?")

Kayla.down()
Isabella.down()
Nat.down()

Winner = ""

while True:
    Nat.seth(random.randint(75, 115))
    Kayla.seth(random.randint(75, 115))
    Isabella.seth(random.randint(75, 115))

    Nat.forward(random.randint(1,20))
    Kayla.forward(random.randint(1,20))
    Isabella.forward(random.randint(1,20))

    if Kayla.ycor() > 250:
        Winner = "Kayla"
        break
    elif Nat.ycor() > 250:
        Winner = "Nat"
        break
    elif Isabella.ycor() > 250:
        Winner = "Isabella"
        break

if Winner == guess:
    print("You guessed correct")
else:
    print("You LOSE")


window.mainloop()




