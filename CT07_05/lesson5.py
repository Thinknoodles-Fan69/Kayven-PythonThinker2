# print("Hello from lesson 5")
import random
import time
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






name = input("What is your name? =")

Pokemon1 = random.choice(pokemons)

Pokemon2= random.choice(pokemons)
while Pokemon2 == Pokemon1:
    Pokemon2= random.choice(pokemons)
Power1Index= pokemons.index(Pokemon1)
Power2Index= pokemons.index(Pokemon2)

Power1 = powers[Power1Index]
Power2 = powers[Power2Index]

if Power1 > Power2:
    higherPower = name
    higherPokemon = Pokemon1
    lowerPower = "ÄI Bot"
    lowerPokemon = Pokemon2
else:
    higherPower = "ÄI Bot"
    higherPokemon = Pokemon2
    lowerPower = name
    lowerPokemon = Pokemon1





print("Welcome, one and all, to this momentous occasion! Today marks the 50th anniversary pokemon competition final—a place where the best Pokemon player win the grand champion and is titled the world best Pokemon Player. We gather here not just to celebrate a Winner, but to embrace the future. Let the competition begin!")
time.sleep(20)
print("Here are the rules:")
time.sleep(3)
print("Each player has a random pokemon with a power to it. Whoever's pokemon power is greater, will win the competition. Let the games begin!")
time.sleep(10)

print(name + " pokemon is the " + Pokemon1 + ". Will he/she achieve victory with this pokemon? Let us give him/her a round of applause for him/her getting a good pokemon!")
time.sleep(10)
print("AI bot pokemon is the " + Pokemon2 + ". Will he achieve victory with this pokemon? Let us give him a round of applause for him getting a good pokemon!")
time.sleep(10)

print("Now, Let the games begin!")
time.sleep(3)
print("Players, please get ready and enter to battle field.")
time.sleep(3)
print("Players, it is time to fight.")
time.sleep(3)

for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

print("The fight begins with " + lowerPokemon + " using his super move against " + higherPokemon + ". But " + higherPokemon + " escaped without a scratch on its body. Instead, " + higherPokemon + " Started a counter attack!" )
time.sleep(8)
print(higherPokemon + " used his ability to blind " + lowerPokemon + " eyes! What a way to stun the opponent! " + higherPokemon + " tried to use his super move against " + lowerPokemon + ", but it was defended as " + lowerPokemon + " used his hearing to hear where the souds of " + higherPokemon + " is and blocked its attack. What a brilliant move!")
time.sleep(20)
print("This is a crazy and intense match, But who will win?")
time.sleep(3)
print("Bang!")
time.sleep(2)
print(lowerPokemon + " used his mega evolution and stomped on " + higherPokemon + ". " + higherPokemon + " fell onto the ground in pain. Looks like " + lowerPower + " is going to win this competition!")
time.sleep(7)
print("Looks like " + lowerPower + " and " + lowerPokemon + " is celebrating their win!")
time.sleep(3)
print("Wait! But " + higherPokemon + " is nowhere to be seen! Where is " + higherPokemon + "?")
time.sleep(3)
print("Wait! Is that " + higherPokemon + "? Looks like " + higherPower + " used the Double Rush!")
time.sleep(3)
print("Bang! Smack! Looks like " + higherPokemon + " attack his opponent Pokemon twice. Looks like " + lowerPokemon + " is lying unconscious on the ground!")
time.sleep(10)
print("The referee is going to start the countdown")
time.sleep(5)
for a in range(1, 11 ):
    print(a)
    time.sleep(1)

print("Game over! " + lowerPower + " Pokemon is unable to battle!")
time.sleep(1)
print("The game is finally over! Looks like there is a winner!")

time.sleep(5)
print("The winner of this exciting match with consist of AI bot and " + name + " is........... " + higherPower + " and his pokemon " + higherPokemon + ". Lets congratulate them for being the winner of the competition and lets give him/her the trophy. Ronud of applause everyone!")
