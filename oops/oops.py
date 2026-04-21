# class Account:
#     def __init__(self,balance):
#         self.__balance = balance 


#     def getBalance(self):
#         print("validating the user")
#         return self.__balance    
    
#     def setBalance(self,balance):
#         print("validating the user")
#         self.__balance = balance


# class Animal:
#     def __init__(self):
#         pass 
#     def walk(self):
#         print("Animal is walking")

#     def speak(self):    
#         print("Animal makes a sound")

#     def eat(self):
#         print("Animal is eating")

# class Cat(Animal):

#     def speak(self):
#         print("Cat says meow")

#     def eat(self):
#         super().eat()
#         print("Cat is munching on fish")

# class Kitten(Cat):

#     def eat(self):
#         super().eat()
#         print("kitten drinks milk")


# k = Kitten()
# k.eat()             

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass 

class Circle(Shape):   

    def area(self,r):
        return 3.14 * r * r 
    
c = Circle()
print(c.area(2))    