# print("Hello from lesson 7")


# contacts = []
# contact1 = ["Kayla", 88278202, "Becoming a girl"]
# contact2 =  ["Min Yan", 81385653, "Singing Skibidi Toilet"]
# contact3 = ["Jade", 91513613, "Eating Human Flesh"]
# contacts.append(contact1)
# contacts.append(contact2)
# contacts.append(contact3)
# for contactses in contacts:
#     name, phoneno, cca = contactses
#     print("Name:" + name)
#     print("Phone Number:" + str(phoneno))
#     print("CCA:" + cca )
    



# list1 = ["Apple", "Banana", "Cherry"]
# list2 = ["Durian", "Elderberry", "Figs"]

# listses = list1 + list2

# print(listses)

# list1 = [3.20, 2.65, 1.75]
# list2 = [6.15, 5.45, 4.20]

# listses = list1 + list2
# sortedlistses = sorted(listses)
# print(sortedlistses)

# fruits = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Figs"]
# index = 3
# print(fruits[:index])
# print(fruits[index:])

# fruits = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Figs"]
# midIndex = len(fruits)//2
# print(fruits[:midIndex])
# print(fruits[midIndex:])


# list1 = ["Apple", "Banana", "Cherry", "Durian"]
# list2 = ["Cherry", "Durian", "Elderberry", "Figs"]
# common = []

# for i in list1:
#     if i in list2:
#         common.append(i)

# for a in common:
#     print(a)






# list1 = ["Apple", "Banana", "Cherry", "Durian"]
# list2 = ["Cherry", "Durian", "Elderberry", "Figs"]
# common = []

# for a in list1:
#     if a in list2:
#         common.append(a)

# print(common)


# list1 = ["Apple", "Banana", "Cherry", "Durian"]
# list2 = ["Cherry", "Durian", "Elderberry", "Figs"]
# unique = []

# for i in list1:
#     if i not in list2:
#         unique.append(i)

# for i in list2:
#     if i not in list1:
#         unique.append(i)

# for a in unique:
#     print(a)



# TRY FIRST

# list1 = ["Apple", "Banana", "Cherry", "Durian"]
# list2 = ["Cherry", "Durian", "Elderberry", "Figs"]
# unique = []

# for i in list1:
#     for a in list2:
#         if i != a:
#             unique.append(i)

# for a in list2:
#     for i in list1:
#         if a != i:
#             unique.append(a)

# print(unique)


# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]
# even = []
# listses = list1 + list2
# for i in listses:
#     if ( i % 2) == 0:
#         even.append(i)

# for a in even:
#     print(a)


# nested_list = [[1, 2], [3, 4], [5, 6]]
# flat_list = []
# for noses in nested_list:
#     for nos in noses:
#         flat_list.append(nos)
# for a in flat_list:
#     print(a)

# students = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# size = 3
# nested_list = []
# for i in range(0, len(students) , size):
#     nested_list.append(students[i:i+size])

# for a in nested_list:
#     print(a)


 
# Second TRY
# students = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# size = 3
# nestedList = []
# for i in range(0, len(students), size):
#     nestedList.append(students[i:i+size])

# print(nestedList)







