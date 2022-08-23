from genericpath import isdir
import json
import os

from models import Asteroid
from categorizing import Categorizer

path = "./Asteroids/"

class DataReader:
    asteroid_paths: list[str] = []
    asteroids: list[Asteroid] = []
    data_path = path
    
    def __init__(self):
        self.data_path = path
        self.asteroid_paths = os.listdir(self.data_path)
      
    def get_asteroid_info(self):
        for p in self.asteroid_paths:
            json_string = open(self.data_path + p, "r").read()
            obj = json.loads(json_string)
            asteroid = Asteroid(obj["metals"], obj["name"], True if obj["worth"] == "True" else False)
            print(asteroid)

            self.asteroids.append(asteroid)
        
        print(self.asteroids)
        return self.asteroids
    

class DataWriter:
    @staticmethod
    def make_new_asteroid():
        if not os.path.isdir(path):
            os.mkdir(path)
        
        iron_amount = int(input("Iron amount: "))
        silver_amount = int(input("Silver amount: "))
        gold_amount = int(input("Gold amount: "))
        platinum_amount = int(input("Platinum amount: "))
        
        materials = [["Iron", iron_amount], ["Silver", silver_amount], ["Gold", gold_amount], ["Platinum", platinum_amount]]

        asteroid = Asteroid(materials)
        Categorizer.categorize([asteroid])
        
        obj = {
            "name": asteroid.name,
            "metals": asteroid.metals,
            "worth": "True" if asteroid.worth else "False"
        }
        
        asteroid_json = json.dumps(obj)

        file = open(path + asteroid.name + ".json", "w")
        file.write(asteroid_json)


DataWriter.make_new_asteroid()

reader = DataReader()
reader.get_asteroid_info()