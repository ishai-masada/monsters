import random

def display():
    print(f'Inventory: {inventory} \n', f'Health: {hp}', f'Strength: {strength}')

print("Welcome to Conquest! \n", "Your goal is to conquer every planet and establish peace.")
input("press enter to start the first battle...")

creatures = ["bitbit", "mantois", "rocklit"]
planets = ["mars \'r us", "pluutoen", "darkusus"] 

inventory = []
hp = 100
enemy_hp = 50
strength = 10
enemy = random.choice(creatures).title()
destination = random.choice(planets)

print(f"The first battle is with a {enemy} on planet {destination} \n")
print("{enemy} has an hp of 50 and a strength of 4. Diminish its health to defeat the creature.")
print("\nThese are your stats: ")
display()

while hp > 0 and enemy_hp > 0:
    count = 1
    # enemy turn
    if count % 2 == 0:
        print(f"{enemy} attacks you!")
        if random.choice(True, False) == True:
            hp -= 4
            print("{enemy}'s attack hit you!"})
        else:
            print("{enemy}'s attack missed you!"})
    else:
        #player turn
        choice = input("It's time to act!. Either attack or run away like a coward. Type either \'attack\', or \'run\'."
                       "Any misspelling will result in a redo.")
        if choice == "attack":
            if random.choice(True, False) == True:
                enemy_hp -= 4
                print("Your attack hit the {enemy}!"})    
            else:
                    print("Your attack missed! You stoopid"})
        elif choice == "run":
            if random.choice(True, False) == True:
                print("You ran away from your duty you cooward!")
                break
            else:
                print("You failed to run away you cooward!")
                continue
        # else:
