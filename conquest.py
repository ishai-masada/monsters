import random

def display():
    print(f'\nInventory: {inventory}', f'\nHealth: {hp}', f'\nStrength: {strength}')

def enemy_display():
    print(f'\nName: {enemy}', f'\nHealth: {enemy_hp}', f'\nStrength: 4')

def rand_bool():
    return random.choice([True, False])

# Start of the game
print("Welcome to Conquest!", "\nYour goal is to conquer every planet and establish peace.")
input("press enter to start the first battle...")

creatures = ["bitbit", "mantois", "rocklit", "pythooner", "dragoooner", "moonkier", "woorm"]
planets = ["mars \'r us", "pluutoen", "darkusus"] 

inventory = []
hp = 100
enemy_hp = 50
strength = 10
enemy =random.choice(creatures).title()
destination = random.choice(planets)
victory = True

print(f"The first battle is with a {enemy} on planet {destination} \n")
print(f"{enemy} has an hp of 50 and a strength of 4. Diminish its health to defeat it!")
print("\nThese are your stats: ")
display()

count = 1
while hp > 0 and enemy_hp > 0:
    # Enemy turn
    if count % 2 == 0:
        print(f"{enemy} attacks you!")
        if random.choice(True, False) == True:
            hp -= 4
            print("{enemy}'s attack hit you!\n")
            display()
        else:
            print("{enemy}'s attack missed you!\n")
            display()
    # Player turn
    else:
        # Action prompt
        while True:  
            choice = input("\nIt's time to act!. Either attack or run away like a cooward. Type either \'attack\', or \'run\'. "
                           "\nYou will have to retype your input if you misspell it: ")
            # Check if the input is spelled correctly
            if choice in ['attack', 'run']:
                break
            # Create an error if it isn't spelled correctly
            print("\nYour input did not read as \"attack\" or \"run\".")

        # Check if it's attack
        if choice == "attack":
            if rand_bool():
                enemy_hp -= 10
                print("\nYour attack hit the {enemy}!") 
            else:
                print("\nYour attack missed! You stoopid.")
            enemy_display()
        # Check if it's run
        elif choice == "run":
            if rand_bool():
                print("\nYou ran away from your duty you cooward!")
                break
            else:
                print("\nYou failed to run away you cooward!")
                continue
        # Checks for victory or loss each round of turns
        if hp<0 and enemy_hp>0:
            victory = False
            print("\nYou have lost! Return to the home you came from.")
            break
        elif hp>0 and enemy_hp<0:
            print("\nYou have defeated your enemy and attained victory! Congratulations!")
            break
        count += 1
