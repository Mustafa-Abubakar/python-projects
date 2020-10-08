class Pet:
    def __init__(self):
        self.__name = 'Pet'
        self.__animal_type = "Bird"
        self.__age = "3 months"
    
    def set_name(self, name):
        self.__name = name
    
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
    
    def set_age(self, age):
        self.__age = age
    
    def get_name(self):
        return self.__name
    
    def get_animal_type(self):
        return self.__animal_type
    
    def get_age(self):
        return self.__age


def main():
    animal = Pet()
    animal.set_name('Pipi')
    animal.set_animal_type('Cat')
    animal.set_age('2 years')
    name = animal.get_name()
    animal_type = animal.get_animal_type()
    age = animal.get_age()
    print('Animal name: '+name+'\nAnimal type: '+animal_type+'\nAnimal age: '+age)


main()
