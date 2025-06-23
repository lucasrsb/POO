class Animal:
    def sound(self):
       return "Animal fala"

class Cachorro(Animal):
    def sound(self):
        return "Au au"
    
class Gato(Animal):
    def sound(self):
        return "Miau"

ANIMAL = {
    "gato": Gato,
    "cachorro": Cachorro
}

name_input = input()
animal = ANIMAL.get(name_input, Animal)()
print(animal.sound())
    

