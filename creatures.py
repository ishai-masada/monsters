import json

class Creature:

    def __repr__(self):
        return f"<Name: {self.name}, Health: {self.hp}>"

    def __init__(self, level, name, _type, hp, strength, defense, accuracy, resistance, speed, abilities):
        self.level = level
        self.name = name
        self.type = _type
        self.hp = hp
        self.strength = strength
        self.speed = speed
        self.defense = defense
        self.accuracy = accuracy
        self.resistance = resistance
        self.abilities = abilities

    @classmethod
    def from_json(cls, creature_json):
        return cls(level=creature_json['level'], _type=creature_json['type'], name=creature_json['name'], hp=creature_json['hp'], strength=creature_json['strength'], defense=creature_json['defense'], accuracy=creature_json['accuracy'], resistance=creature_json['resistance'], speed=creature_json['speed'], abilities=creature_json['abilities'])

if __name__ == '__main__':
    with open('creatures.json', 'r') as f:
        creature_json = json.load(f)

    creatures = {}
    for name, stats in creature_json.items():
        creatures[name] = Creature.from_json(stats)

def hard_punch(enemy):
	enemy.hp -= 15 
	return f'enemy hp is now: {enemy.hp}'

def wiggle(enemy):
	enemy.hp -= 17
	return f'enemy hp is now: {enemy.hp}'

def fire_attack(enemy):
	enemy.hp -= 20
	return f'enemy hp is now: {enemy.hp}'

def nibble(enemy):
	enemy.hp -= 9
	return f'enemy hp is now: {enemy.hp}'

def crush(enemy):
	enemy.hp -= 3
	return f'enemy hp is now: {enemy.hp}'

def spear_attack(enemy):
	enemy.hp -= 3
	return f'enemy hp is now: {enemy.hp}'

def sting(enemy):
	enemy.hp -= 15
	return f'enemy hp is now: {enemy.hp}'
