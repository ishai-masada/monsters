import random
import items
import abilities
from copy import deepcopy
import json
from planets import Planet
from models import Creature

def display():
    print(f'\nInventory: {Inventory}', f'\nName: {player.name}', f'\nType: {player.type}', f'\nLevel: {player.level}', f'\nHealth: {player.hp}', f'\nStrength: {player.strength}', f'\nDefense: {player.defense}', f'\nSpeed: {player.speed}', f'\nAccuracy: {player.accuracy}', f'\nResistance: {player.resistance}')

def enemy_display(enemy):
    print(f'\nName: {enemy.name}', f'\nType: {enemy.type}', f'\nLevel: {enemy.level}', f'\nHealth: {enemy.hp}', f'\nStrength: {enemy.strength}', f'\nDefense: {enemy.defense}', f'\nSpeed: {enemy.speed}', f'\nAccuracy: {enemy.accuracy}', f'\nResistance: {enemy.resistance}')

def rand_bool():
    return random.choice([True, False])

def load_creatures():
    with open('creatures.json', 'r') as f:
        creatures_json = json.load(f)

    creatures = {}
    for name, stats in creatures_json.items():
        creatures[name] = Creature.from_json(stats, abilities_map)
    return creatures

def load_planets():
    with open('planets.json', 'r') as f:
        planets_json = json.load(f)

    planets = []
    for planet in planets_json.get("planets"):
        planets.append(Planet.from_json(planet))
    return planets

def enumeration(enumeratable):
    if enumeratable == player.abilities:
        print(f'\nYour abilities:')
        for i, ability in enumerate(enumeratable):
            print(f'\t{i + 1} - {ability}')
    elif enumeratable == Inventory:
        print(f'\nYour items:')
        for i, enumeration.item_name in enumerate(enumeratable):
            print(f'\t{i + 1} - {enumeration.item_name}')

def enemy_attack(enemy, player, Inventory):
    enemy_attack = random.choice(enemy.abilities) 
    abilities_map[enemy_attack](enemy, player)
    print(f'\n{enemy.name} attacks you with {enemy_attack}!')
    if player.hp < 0:
        player.hp = 0
    else:
        display()

def battle_attack(player, enemy, Inventory):
    enumeration(player.abilities)
    while True:
        option = input('\nEnter the attack you want: ')
        try:
            index = int(option) - 1
            if index in range(len(player.abilities)):
                attack = player.abilities[index]
                print(f'\nYou attack the {enemy.name} with {attack}!')
                if rand_bool():
                    print(f'\nYour attack hit the {enemy.name}!')
                    abilities_map[attack](player, enemy)
                    if enemy.hp < 0:
                        enemy.hp = 0
                    else:
                        enemy_display(enemy)
                else:
                    print(f'\nYour attack missed the {enemy.name}!')
                break 
            else:
                print('Attack doesn\'t exist')
        except ValueError:
            if option == 'back':
                return 'back'
            else:
                print('\nYour input was not a valid attack')

def battle_run(player, enemy, Inventory):
    if rand_bool():
        print("\nYou ran away from your duty you cooward!")
        return 'break'
    else:
        print("\nYou failed to run away you cooward!")
        return 'continue'

def battle_items(player, enemy, Inventory):
    enumeration(Inventory)
    while True:
        option = input('Enter the item you want to use: ')
        try:
            index = int(option) - 1
            if index in range(len(Inventory)):
                item = Inventory.pop(enumeration.item_name)
                item(player, enemy)
                print('You have healed yourself!')
                display()
            elif len(Inventory) == 0:
                print('Inventory is empty')
            else:
                print('Item doesn\'t exist')
        except ValueError:
            if option == 'back':
                return 'back'
            else:
                print('\nYour input was not an item in your Inventory')

def battle(idx, enemy):
    print(f"\nYou are fighting a {enemy.name}!")
    count = 0
    while True:
        count += 1
        # Enemy turn
        if count % 2 == 0:
            enemy_attack(enemy, player, Inventory)
            # Checks for loss 
            if player.hp<=0 and enemy.hp>0:
                player.hp = 0
                display()
                print("\nYou have lost! Return to the home you came from.")
                break
        # Player turn
        else:
            while True: # Loop for the player's turn
                while True:  # Checking what the player wants to do 
                    choice = input("\nIt's time to act!. Either attack, choose an item, or run away like a cooward. Type either \'attack\', \'items\', or \'run\'. "
                                   "\nYou will have to retype your input if you misspell it: ")
                    # Check if the input is spelled correctly
                    if choice in BATTLE_MENU:
                        break
                    # Re-prompts if it isn't spelled correctly
                    print("\nYour input did not read as \"attack\" or \"run\".")
                action = BATTLE_MENU[choice](player, enemy, Inventory)
                if action != 'back':
                    break
            if action == 'break':
                break
            elif action == 'continue':
                continue
        # Checks for victory
        if player.hp>0 and enemy.hp<=0:
            enemy.hp = 0
            enemy_display(enemy)
            # Check to see if the monster is the last monster in the level 
            if idx >= (len(monsters)-1):
                print("\nYou have defeated your enemies and attained victory! Congratulations!")
                break
            else:
                print(f"\nYou have defeated the {enemy.name}!")
            break
    return 0

BATTLE_MENU = {'attack': battle_attack, 'run': battle_run, 'items': battle_items}
abilities_map = {"push": abilities.push, "hard_punch": abilities.hard_punch, "wiggle": abilities.wiggle, "fire_attack": abilities.fire_attack, "nibble": abilities.nibble, "crush": abilities.crush, "spear_attack": abilities.spear_attack, "sting": abilities.sting}

### Start of the game
print("Welcome to Conquest!", "\nYour goal is to conquer every planet and establish peace.")
creatures = load_creatures()
planets = load_planets()

Inventory = {'small_recover': items.small_recover}
# TODO: i want to remove this line
player = creatures['moonkier']
# player = deepcopy(creatures.get(random.choice(list(creatures))))
print(f'player: {player}')
print("\nThese are your stats: ")
display()

level_1 = planets[0].levels[0]
print(f"This is the first level : {level_1}")
monsters = level_1.get('creatures')

for idx, creature in enumerate(monsters):
    monster = deepcopy(creatures.get(creature))
    battle(idx, monster)
