# print("Hello from lesson 8")
list1 = [3, 2, 1]
list2 = [6, 5, 5]
list3 = [9, 8, 7]
newList = []
lista = []
listb = []
daddy = list1 + list2 + list3

newList = sorted(newList)

for letters in daddy:
    if letters in newList:
        newList.append(letters)

midPoint = len(newList) // 2

lista = newList[:midPoint]
listb = newList[midPoint:]

print(lista)
print(listb)