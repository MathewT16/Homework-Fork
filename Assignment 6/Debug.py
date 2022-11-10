class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Employee:
    def __init__(self, name, idNumber, department):
        self.name = name
        self.idNumber = idNumber
        self.department = department
        
class Cake:
    #can you fill out the rest of this for me? im dumb
    #the cake needs to have the cake flavor and cake frosting stored
    def __init__(self,flavor,frosting_Stored):
        self.flavor = flavor
        self.frosting_Stored = frosting_Stored
        
def main():
    #fill this one out with a dog's name and age.. can be your dog, friend's dog, etc
    newDog = Dog("Scooby Doo" , 62)
    print(newDog.name, newDog.age)
    
    #and what about a new employee
    newEmployee = Employee("Joe Biden", 46, "Presidency")
    #how would we print out each of the variables from newEmployee?
    print(newEmployee.name,newEmployee.idNumber,newEmployee.department)
    
    #now create and print out a cake you make
    vanillaCake = Cake("Vanilla",100)
    print(vanillaCake.flavor,vanillaCake.frosting_Stored)
    
    
    #and now create another cake and print it out
    bloodCake = Cake("Blood", 100000)
    print(bloodCake.flavor, bloodCake.frosting_Stored)
main()
