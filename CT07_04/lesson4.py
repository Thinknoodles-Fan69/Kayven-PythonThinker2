# print("Hello from lesson 4")
Solar = [
    "Mercury",
    "Venus",
    "Earth",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Nepture"
]


# Solar.pop(4)
# print(Solar)




# Solar.append("Pluto")
# Solar.insert(3, "lalaLand")

earth_index = Solar.index("Earth")
Solar.insert(earth_index + 1, "LalaLand")

# Solar[3] = "Skibidi Ohio Sigma Rizzler Gyatty Ligma Kissma Toilet Bowl"
# print(Solar)

# zoo = [
#     "monkey",
#     "lion", 
#     "deer",
#     "tiger",
#     "elephant",
#     "kangaroo"
# ]

# zoo.pop()
# print(zoo)





# counter = 0

# while counter != len(zoo):
#     print(zoo[counter])    
#     counter +=1



# zoo.insert(10, "Foxhole")
# print(zoo)

# for i in Solar:
#     if i == "Earth":
#         print( i + ": this is my home")
#     elif i == "Mars":
#         print( i + ": I conquered this")
#     elif i == "LalaLand":
#         print(i + ": I created this")
#     else:
#         print(i)


# country = []
# while True:
#     user = input("What Country do you want to visit? = ")
#     if user == "end":
#         break
#     country.append(user)
# for i in country:
#     print("I would like to visit " + i)



Food = []
while True:
    user = input("What Food do you want to sell? = ")
    if user == "end":
        break
    Food.append(user)

while True:
    person = input("What would you like to eat? = ")
    print(Food)
    for i in Food:
        print(i)       
        if person == i:
            print("Yes! We sell that! Please have a seat.")
            break
        else:
            print("Sorry, please go next door. Bye!")
            break
        
    break