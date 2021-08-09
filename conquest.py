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

def battle_attack(player, enemy):
    print(f'\nYour abilities: {player.abilities}')
    while True:
        option = input('\nEnter the attack you want: ')
        if option in abilities_map:
            print(f'\nYou attack the {enemy.name} with {option}!')
            break 
        else:
            print('\nYour input was not a valid attack')
    if rand_bool():
        print(f'\nYour attack hit the {enemy.name}!')
        abilities_map[option](player, enemy)
        if enemy.hp < 0:
            enemy.hp = 0
        else:
            enemy_display(enemy)
    else:
        print(f'\nYour attack missed the {enemy.name}!')
    return 0

def battle_run(player, enemy):
    if rand_bool():
        print("\nYou ran away from your duty you cooward!")
        return 'break'
    else:
        print("\nYou failed to run away you cooward!")
        return 'continue'

def battle_items(player, enemy, Inventory):
    print(f'Inventory: {Inventory}')
    Inventory.pop(input('Enter the item you want to use: '))
    print(f'Inventory: {Inventory}')

def battle(idx, enemy):
    print(f"\nYou are fighting a {enemy.name}!")
    count = 0
    while True:
        count += 1
        # Enemy turn
        if count % 2 == 0:
            print(f"\n{enemy.name} attacks you!")
            if rand_bool():
                player.hp -= 4
                print(f"\n{enemy.name}'s attack hit you!")
                display()
            else:
                print(f"\n{enemy.name}'s attack missed you!")
                display()
        # Player turn
        else:
            # Action prompt
            while True:  
                choice = input("\nIt's time to act!. Either attack or run away like a cooward. Type either \'attack\', or \'run\'. "
                               "\nYou will have to retype your input if you misspell it: ")
                # Check if the input is spelled correctly
                if choice in BATTLE_MENU:
                    break
                # Create an error if it isn't spelled correctly
                print("\nYour input did not read as \"attack\" or \"run\".")
            prompt = BATTLE_MENU[choice](player, enemy)
            if prompt == 'break':
                break
            elif prompt == 'continue':
                continue
        # Checks for victory or loss each round of turns
        if player.hp<=0 and enemy.hp>0:
            player.hp = 0
            display(player)
            print("\nYou have lost! Return to the home you came from.")
            break
        elif player.hp>0 and enemy.hp<=0:
            enemy.hp = 0
            enemy_display(enemy)
            # Checks to see if the monster is the last monster in the level 
            if idx >= (len(monsters)-1):
                print("\nYou have defeated your enemies and attained victory! Congratulations!")
                break
            else:
                print(f"\nYou have defeated the {enemy.name}!")
            break
    return 0

BATTLE_MENU = {'attack': battle_attack, 'run': battle_run}
abilities_map = {"hard_punch": abilities.hard_punch, "wiggle": abilities.wiggle, "fire_attack": abilities.fire_attack, "nibble": abilities.nibble, "crush": abilities.crush, "spear_attack": abilities.spear_attack, "sting": abilities.sting}
items_map = {"small_recover": items.small_recover}

### Start of the game
print("Welcome to Conquest!", "\nYour goal is to conquer every planet and establish peace.")
creatures = load_creatures()
planets = load_planets()

Inventory = []
Inventory.append(items_map["small_recover"])
player = deepcopy(creatures.get(random.choice(list(creatures))))
print(f'player: {player}')
print("\nThese are your stats: ")
display()

level_1 = planets[0].levels[0]
print(f"This is the first level : {level_1}")
monsters = level_1.get('creatures')

for idx, creature in enumerate(monsters):
    monster = deepcopy(creatures.get(creature))
    battle(idx, monster)
