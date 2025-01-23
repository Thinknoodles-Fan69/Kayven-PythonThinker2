# print("Hello from lesson 2")

# for i in range(500):
#     print("I will not sling muds at my friends again")


# print("Hello")
# for outer in range(5):
#     print("la la la")
#     for inner in range(2):
#         print("ba ba ba")
#     print("cha cha cha")
# print("bye") 


# for i in range(0, 21):
#     print(i)


# for i in range(1, 31):
#     print(i)

# for i in range(2, 25, 2):
#     print(i)


# counter = 0
# while counter < 21:
#     print(counter)
#     counter += 1


# count = 1
# while count < 31:
#     print(count)
#     count += 1

# counts = 2
# while counts < 25:
#     print(counts)
#     counts += 1


# counting = 1
# while counting <= 10:
#     if counting == 5:
#         break
#     print(counting)
#     counting += 1



# counting = 1
# while counting < 10:
#     while counting == 5:
#         break
#     else:
#         print(counting)
#         counting += 1


# no = 1
# while no != 11:
#     print(no)
#     no += 1
# else:
#     print("count has reached 10")


# no = 1
# while no != 11:
#     print(no)
#     no += 1
#     if no == 5:
#         break
# else:
#     print("count has reached 10")

# topping = "Here are your toppings on your pizza: "
# while True:
#     item = str(input("What topping do you want pizza? Name them one by one.If thats all, Type 'END'  :"))
#     if item.lower() == "End".lower():
#         break
#     topping += ", " + item

# print(topping)


score = 0
while True:
    


    for i in range(5):
        if i != 5:
            answer = input("If a bat and a baseball bat cost $1.10, and the baseball bat is $1 more than the bat, how much is the bat?")

            if answer == "$0.05" or answer == "5¢" or answer == "5 cents" or answer == "five cents" or answer == "5 cent" or answer == "five cent":
                print("correct!")
                score += 1
                break
            else:
                print("That is wrong! Try again")

        else:
            print("You have answersed to many times. Please proceed to the next question")
            break
        

    
            
        

   

    for i in range(5):
        if i != 5:
            answer = input("If 5 machine in 5 minutes prints 5 paper, how long does it takes for 100 machines to print 100 paper?")

            if answer == "5" or answer == "five":
                print("correct!")
                score += 1
                break
            else:
                print("That is wrong! Try again")

        else:
            print("You have answersed to many times. Please proceed to the next question")
            break




    

    for i in range(5):
        if i != 5:
            answer = input("There is a lilypad in your pond, and it doubles everyday. At day 50, the lilypad covered the entire pond.How many days does it take the lilypad to cover half the pond?")

            if answer == "49" or answer == "fourty-nine":
                print("correct!")
                score += 1
                break
            else:
                print("That is wrong! Try again")

        else:
            print("You have answersed to many times. Please proceed to the next question")
            break


    print("Your score is " + str(score))

    break



## Define my variables
# max_attempts = 3
# score = 0

# questions_answers = [
#     "qn1?", "ans1",
#     "qn2?", "ans2", 
#     "qn3?", "ans3"
# ]

# for i in range(0, len(questions_answers), 2):
#     question = questions_answers[i]
#     answer = questions_answers[i + 1]
#     attempts = 0

#     while attempts < max_attempts:
#         user_input = input(question)
        
#         if user_input.lower() == answer.lower():
#             score += 1
#             print("Correct!")
#             break
#         elif user_input.lower() == "skip":
#             print("Question skipped.")
#             break
#         else:
#             print("Wrong!")
#             attempts += 1

#         if attempts == max_attempts:
#             print("Too many attempts! Try the next question.")

# print(f"Your final score is {score} out of {len(questions_answers) // 2}.")










Question = "What is for breakfast? = "
answer = "Stale chips with Skibidi Ohio Sigma Rizzler Gyatty Ligma Kissma Toilet Bowl Sauce"
guess = input(Question)
while guess != answer:
    print("Wrong! Are you freaking kidding me? It is so easy bruh. How hard it is? You did not even try your best lol. I will send you to Jesus!!!!!!!!!!!!!!")
