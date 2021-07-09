
import json

class Planet:

    def __repr__(self):
        return f"<Name: {self.name}>"

    def __init__(self, number_of_levels, name, levels):
        self.level = number_of_levels,
        self.name = name
        self.levels = levels

    @classmethod
    def from_json(cls, planet_json):
        return cls(name=planet_json["name"], number_of_levels=planet_json["number_of_levels"], levels=planet_json["levels"])

if __name__ == '__main__':
    with open('planets.json', 'r') as f:
        planets_json = json.load(f)

    planets = []
    for planet in planets_json().get("planets"):
        planets.append(Planet.from_json(planet))
