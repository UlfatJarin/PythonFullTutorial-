"""warrior_name ='thor'
warrior_health =100
warrior_attack =50

mage_name ="Gandalf"
mage_health = 80
mage_attack = 70

def attack_warrior():
    print(f'Warrior attacks with power',warrior_attack)
def attack_mage():
    print(f'Mage attacks with power',mage_attack)

attack_warrior()
attack_mage()
"""

#code security 

class Character:
    def __init__(self, name , health , attack ):
        self.name =name
        self.health =health
        self.attack = attack
     
    def attack_enemy(self):
        print(f'{self.name} attack with power{ self.attack}')

warrior= Character('thor',100,50)
mage= Character('Gandalf',80,70)

warrior.attack_enemy()
mage.attack_enemy()

"""
classes & objects
inheritance
encapsulation
abstaction 
polymorphism
"""
#classes & objects
# map -class
#house -object

class Car():
    #method
    def start(self):
        print("car is starting")
    def stop(self):
        print("car is stopting")

car1= Car()
car2= Car()

car1.start()
car1.stop()

car2.start()
car2.stop()
 

class Vehical :
    def set_details(self,brand,color):
        self.brand= brand
        self.color= color
    
    def show_ditails(self):
        print(f'This car is a {self.color}{self.brand}')

car1 =Vehical()
car1.set_details('tesla','red')

car2 =Vehical()
car2.set_details('BMW','blue')

car1.show_ditails()
car2.show_ditails()



#constructor 
"""
__init__() #automatic constuctor
no nedd to call method(show_ditails etc)

"""
class Vehical :
    def __init__(self,brand,color):
        self.brand= brand
        self.color= color

car1 =Vehical("tesla",'red')
print(car1.brand, car1.color)

class Student :
    def __init__(self , name , age, grade):
        self.name = name
        self.age = age
        self.grade = grade

student1 = Student('ulfat',23,'A+')
student2 = Student('Jarin',24,'A-')

print(student1.name , student1.age ,student1.grade)
print(student2.name , student2.age ,student2.grade)


"""
default constructor(self)
parameterized constructor (self,name,age)
constuctor with defult values(self, name ="unknown", age=0)
"""

#polymorpthism 
"""
one name ,many forms

run
person can run fast
car runs on petrol 
computer program run smoothly

1 word = run
"""
print(len('python'))
print(len({1,2,3}))
print(len({"a":1 , "b": 2 , "c":4}))

#polymorphism with classes

class Bird():
    def sound(self):
        print("Birds make  sounds ")

class Crow(Bird):
    def sound(self):
        print('Crow make  sounds "Caw Caw"')

class Parrot(Bird):
    def sound(self):
        print('Parrot make  sounds "squawk"')

bird1= Crow()
bird2= Parrot()

bird1.sound()
bird2.sound()

#encapsulation
# hide main code 
#
class BankAccount:
    def __init__(self , account_number , balance):
        self.account_number = account_number
        self.__balance =balance     #hide , cannot accessable

    def deposit(self,amount):
        self.__balance += amount
        print(f'Deposited{amount}.New balance{self.__balance}')

    def get_balance(self):
        return self.__balance
    
account = BankAccount('123456',5000)

account.deposit(2000)
print(account.get_balance())


#inheritance
class Animal:
    def speak(self):
        print('Animals make sounds')

class Dog(Animal):
    def bark(self):
        print('Dogs bark')

dog = Dog()
dog.speak()
dog.bark()


# Data abstraction
# hide complex ditails 

from abc import ABC, abstractmethod

class Vehical(ABC):
    @abstractmethod
    def start(self):
        pass # no implementation

class Car(Vehical):
    def start(self):
        print("Car starts with a key")

class Bike(Vehical) :
    def start(self):
        print('Bike starts with a button')

car =Car()
bike = Bike()

car.start()
bike.start()


