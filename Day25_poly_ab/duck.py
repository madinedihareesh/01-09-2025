class Dog:
    def talk(self):
        print('Dog Talks')

    def walk(self):
        print('Dog walks') 

class Duck:
    def talk(self):
        print('Duck Talks')

               

dog=Dog()
duck=Duck()


def person(pet):
    pet.talk()
    if hasattr(pet,'walk'):
        pet.walk()        


person(duck)    