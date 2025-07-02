class Animal:
    def sound(self):
       return "Animal fala"

class Cachorro(Animal):
    def sound(self):
        return "Au au"
    
class Gato(Animal):
    def sound(self):
        return "Miau"

animal_classes = {
    "gato": Gato,
    "cachorro": Cachorro
}

name_input = input()
while True:
    if name_input == "fim": break
    animal = animal_classes.get(name_input, Animal)()
    print(animal.sound())
    name_input = input()
    

