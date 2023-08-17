import copy

class StuffedAnimalPrototype:
    def clone(self):
        pass

class Bear(StuffedAnimalPrototype):
    def clone(self):
        return copy.copy(self)

class Rabbit(StuffedAnimalPrototype):
    def clone(self):
        return copy.copy(self)

class Elephant(StuffedAnimalPrototype):
    def clone(self):
        return copy.copy(self)

# Usage
bear_prototype = Bear()
rabbit_prototype = Rabbit()
elephant_prototype = Elephant()

stuffed_animals = []

for _ in range(5):
    stuffed_animals.append(bear_prototype.clone())

for _ in range(3):
    stuffed_animals.append(rabbit_prototype.clone())

for _ in range(4):
    stuffed_animals.append(elephant_prototype.clone())

for idx, animal in enumerate(stuffed_animals, start=1):
    print(f"Stuffed Animal {idx}: {animal}")