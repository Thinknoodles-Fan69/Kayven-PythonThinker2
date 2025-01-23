# print("Hello from lesson 3")
import time
import random

# Question = "What is for breakfast? = "
# answer = "Stale chips with Skibidi Ohio Sigma Rizzler Gyatty Ligma Kissma Toilet Bowl Sauce"
# guess = input(Question)
# while guess != answer:
#     print("Wrong! Are you freaking kidding me? It is so easy bruh. How hard it is? You did not even try your best lol. I will send you to Jesus!!!!!!!!!!!!!!")
#     guess = input(Question)

# print("Finally correct. HAIYAAA why you take so long?????????Stooopid")



# CountDown = 10
# while CountDown != 0:
#     print(CountDown)
#     CountDown -= 1
#     time.sleep(1)
# print("Throw Big boy down!!")


# timing = int(input("How long do you want to study? Minutes = ")) * 60
# while timing != 0:
#     print(str(timing) + " second left bruh.......")
#     timing -= 1
#     time.sleep(1)
# print("Time is up")

# saving = 0
# while saving < 100:
#     question = float(input("How much do you save today after in school, eating recess, eating lunch, buying football card, betting with your friends, eating dinner, going to the movie, paying money to have some rest, wasting the aircon electricity?"))
#     saving += question

# print("You finally after 69420 lives saved $100 and more! Why u waste all your money and when into debt bruh. You should lister to your mama and save all the money you got so in 1 day you could have a=saved 100 already. You need to clear your debt now!!!!!!!!")

lives = 3
question = 1
while question != 15:
    Num = random.randint(2, 20)
    Num1 = random.randint(2, 20)
    ask = input("What is " (Num) + "x " + (Num1) + "?" )
    if ask != Num * Num1:
        print("You are dumb. Wrong!!")
        lives -= 1
    if lives == 0:
        print("You stoopid Lose! You ")    



