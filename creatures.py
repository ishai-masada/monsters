import json
import conquest
import abilities

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
    def from_json(cls, creature_json, functions):

        # iterate over all of the abilities of the given creature
        for ability_name in creature_json['abilities']:
            actions = []
            # Get the corresponding function of each ability name and add it to the actions list
            actions.append(conquest.abilities_map.get(ability_name))
            print(actions)
            return actions

        return cls(level=creature_json['level'], _type=creature_json['type'], name=creature_json['name'], hp=creature_json['hp'], strength=creature_json['strength'], defense=creature_json['defense'], accuracy=creature_json['accuracy'], resistance=creature_json['resistance'], speed=creature_json['speed'], abilities=actions)

abilities_map = {"hard_punch": abilities.hard_punch, "wiggle": abilities.wiggle, "fire_attack": abilities.fire_attack, "nibble": abilities.nibble, "crush": abilities.crush, "spear_attack": abilities.spear_attack, "sting": abilities.sting}

if __name__ == '__main__':
    with open('creatures.json', 'r') as f:
        creature_json = json.load(f)

    creatures = {}
    for name, stats in creature_json.items():
        creatures[name] = Creature.from_json(stats, abilities_map)
