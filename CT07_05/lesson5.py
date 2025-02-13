# print("Hello from lesson 5")
import random
# food = [    
#     "Chicken Rice",
#     "Ice cream",
#     "Avacado From Mexico",
#    "Chocolate Ice Blended",
#     "Chilli"
# ]
# food.pop(2)
# food.append("Mee")
# for i in food:
#     print(i)


# number = []
# counter = 0
# while True:
#     if counter != 100:
#         number.append(random.randint(1, 1000))
#         counter += 1
#     else:
#         break

# for i in number:
#     print(i)



# number1 = []
# counter1 = 0
# while counter1 != 100:
#     no = random.randint(1, 1000)
#     if no not in number1:
#         number1.append(no)
#         counter1 += 1

# for i in number1:
#     print(i)

# print("There is " + len(number1) + " numbers in this list.")


# number1 = []
# counter1 = 0
# while counter1 != 100:
#     no = random.randint(1, 1000)
#     if no not in number1:
#         number1.append(no)
#         counter1 += 1

# print(max(number1))
# print(min(number1))
# print(sum(number1) / len(number1))

# namelist = ["Olivia", "Liam", "Emma", "Noah", "Ava", "Ethan",
#             "Sophia", "Lucas", "Mia", "Aiden"
#             ]
# heightlist = [160, 165, 158, 170, 162, 168, 159, 172, 164, 166]

# number = heightlist.index(max(heightlist))
# print(str(namelist[number]) + " is the tallest in the class with a height of " + str(max(heightlist)) + "cm.")
# number1 = heightlist.index(min(heightlist))
# print(str(namelist[number1]) + " is the shortest in the class with a height of " + str(min(heightlist)) + "cm.")


pokemons = [
    "Pikachu", "Charizard", "Bulbasaur", "Squirtle",
    "Jigglypuff", "Meowth", "Psyduck", "Eevee", "Snorlax",
    "Mewtwo", "Lapras", "Gengar", "Dragonite", "Machamp",
    "Arcanine", "Alakazam", "Gyarados", "Vaporeon", "Scyther",
    "Electabuzz"
]

powers = [
    55, 84, 49, 48, 45,
    45, 52, 55, 110, 110,
    85, 65, 134, 130, 110,
    50, 125, 65, 110, 83
]

name = input("What is you name? =")
print("Welcome, one and all, to this momentous occasion! Today marks the 50th anniversary pokemon competition final—a place where the best Pokemon player win the grand champion and is titled the world best Pokemon Player. We gather here not just to celebrate a Winner, but to embrace the future. Let the competition begin!")
print("Here are the rules:")
print("Each player has a random pokemon with a power to it. Whoever's pokemon power is greater, will win the competition. Let the games begin!")
Pokemon1 = random.choice(pokemons)
print(name + " pokemons is the " + Pokemon1 + ". Will he achieve victory with this pokemon? Let us give him a round of applause for him getting a good pokemon!")
Pokemon2= random.choice(pokemons)
while Pokemon2 == Pokemon1:
    Pokemon2= random.choice(pokemons)
print("AI bot pokemons is the " + Pokemon2 + ". Will he achieve victory with this pokemon? Let us give him a round of applause for him getting a good pokemon!")
