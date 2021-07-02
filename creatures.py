import json

class Creature:
    def __init__(self, level, name, type, hp, strength, defense, accuracy, resistance, speed):
        self.level = level
        self.name = name
        self.type = type
        self.hp = hp
        self.strength = strength
        self.speed = speed
        self.defense = defense
        self.accuracy = accuracy
        self.resistance = resistance

    @classmethod
    def from_json(cls, creature_json):
        return cls(level=creature_json['level'], type=creature_json['type'], name=creature_json['name'], hp=creature_json['hp'], strength=creature_json['strength'], defense=creature_json['defense'], accuracy=creature_json['accuracy'], resistance=creature_json['resistance'], speed=creature_json['speed'])

if __name__ == '__main__':
    with open('creatures.json', 'r') as f:
        creatures_json = json.load(f)

    creatures = {}
    for name, stats in creatures_json.items():
        creatures[name] = Creature.from_json(stats)

