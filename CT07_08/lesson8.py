# print("Hello from lesson 8")
list1 = [3, 2, 1]
list2 = [6, 5, 5]
list3 = [9, 8, 7]
newList = []

newList = list1 + list2 + list3

for i in newList:
    for a in i:
        if a in i:
            newList.pop(a+1)


