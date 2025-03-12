# print("Hello from lesson 8")
# list1 = [3, 2, 1]
# list2 = [6, 5, 5]
# list3 = [9, 8, 7]
# newList = []
# lista = []
# listb = []
# daddy = list1 + list2 + list3

# for letters in daddy:
#     if letters not in newList:
#         newList.append(letters)

# newList = sorted(newList)
# midPoint = len(newList) // 2

# lista = newList[:midPoint]
# listb = newList[midPoint:]

# print(lista)
# print(listb)


# My noteses
tele = "91234567"
tele.isdigit()

username = "learner"
username.isalpha()


string = "hello123"

valid = True
for char in string:
    if not string.isdigit() and not string.alpha():
        valid = False
        break

string = "hello123"

string.isalnum()











