# Programming Languages | Python Pet Class
# Imani Candler | 10.18.2024
# Objective: Write a Pet Class that will take user's pet's name, animal type
# and age, then print to screen.

class Pet:
    def _init_(self, name, animalType, age):
       # self._name = name
        self.name = name
        self.animalType = animalType
        self.age = age

      #  self._animal_type = animalType
       # self._age = age

    def set_name(self, name):
        #name = input("Enter the pet's name")
        self.name = name
   
    def set_animal_type(self, animalType):
        #animalType = input("Enter the animal type: ")
        self.animalType = animalType
    
    def set_age(self, age):
       #age = int(input("Enter the pet's age: "))
       self.age = age
    
    def get_name(self):
       # return("Your pet's name is " + {self._name})
        return self.name
   
   
    def get_animal_type(self):
       # return("Your pet's animal type is " + {self._animal_type}) 
        return self.animalType
    
    def get_age(self):
        #return("Your pet's age is " + {self._age})
        return self.age


#name = input("Enter the pet's name: ")

print("------------RESULTS--------------")
name = input("Enter the pet's name: ")
animalType = input("Enter the animal type: ")
age = int(input("Enter the pet's age: "))
Number = Pet()
#print(Number.name)
Number.set_name(name)
Number.set_animal_type(animalType)
Number.set_age(age)
print(Number.get_name())
print(Number.get_animal_type())
print(Number.get_age())