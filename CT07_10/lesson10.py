# print("Hello from lesson 10")
import random

# ans = 0
# one = int(input("Give me your first number:"))
# two = int(input("Give me your second number:"))
# def multiply(no1, no2):
#     print(no1 * no2)

# multiply(one, two)


# def isElderly(age):
#     if age >= 65:
#         return True
    
# if isElderly(age = int(input("How old are you?"))):
#     print("You are eligible for an elderly discount")
# else:
#     print("You are not eligible for an elderly discount")
        
# number = input("What is your phone number")
# def whatsappMe(number):
#     return "Whatsapp me at https://wa.me/65" + number

# print(whatsappMe(number))



number = []
number1 = []
counter1 = 0
while counter1 != 100:
    no = random.randint(1, 1000)
    if no not in number1:
        number1.append(no)
        counter1 += 1
def whatsappMe(number):
    return "Whatsapp me at https://wa.me/65" + number

print(whatsappMe(number))