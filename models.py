import uuid

class Asteroid:
    name = ""
    metals = []
    worth = False
    
    def __init__(self, metals, name="ASTEROID-" + str(uuid.uuid4()), worth=False):
        self.metals = metals
        self.name = name
        self.worth = worth
