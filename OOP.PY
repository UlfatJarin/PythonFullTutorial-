#MAKE A CLASS

class Phone:
    def make_call(self):
        print("making phone call")
    def play_game(self):
        print("playing Game")

p1 =Phone()

print(p1.make_call())
print(p1.play_game())


#adding perametter

class Phone2:
    def set_color(self,color):
        self.color = color
    def set_cost(self, cost):
        self.cost = cost
    def show_color(self):
        return self.color
    def show_cost(self):
        return self.cost
    def play_game(self):
        print("playing game")
    def make_call(self):
        print("making a call")


p2 = Phone2()

p2.set_color('blue')
p2.set_cost(5000)
 
print(p2.show_color())        
print(p2.show_cost())        
print(p2.play_game())     


#a class with constructor

class Employee :
    def __init__(self,name,age,salary,gender):
        self.name= name
        self.age = age
        self.salary = salary
        self.gender = gender

    def employee_details(self):
        print("Name of employee is ",self.name)
        print("Age of employee is ",self.age)
        print("Salary of employee is ",self.salary)
        print("Gender of employee is ",self.gender)


e1 = Employee('Ulfat',25 ,162000 ,'female')
e2 = Employee('jarin',26, 222000,'female')

print(e1.employee_details())




#inheritance in class

class Vehicle:
    def __init__(self,mileage,cost):
        self.mileage = mileage
        self.cost = cost
    def show_details(self):
        print("I am a vehicle")
        print("the mileage is", self.mileage)
        print("the cost is", self.cost)

v1 = Vehicle(300,1000)
print(v1.show_details())


class Car(Vehicle):
    def show_car_details(self):
        print("I am a car")

c1 = Car(199, 33333)
print(c1.show_details())
print(c1.show_car_details())

class Car2(Vehicle):
    def __init__(self,mileage,cost,tyres,hp):
        super().__init__(mileage,cost)
        self.tyres =tyres
        self.hp = hp
    def show_car_details(self):
        print("im a car")
        print ("Number of types are",self.tyres)
        print ("The Horse Power is",self.hp)

c2 = Car2(500,5000000,8,200)
print(c2.show_details())
print(c2.show_car_details())


# types of inheritance

# single
# muliple
# multilevel
#

# multiple (multiple parent - child)
class Parent1:
    def assign_str1(self,str1):
        self.str1 =str1
    def show_str1(self):
        print(self.str1)

class Parent2:
    def assign_str2(self,str2):
        self.str2 =str2
    def show_str2(self):
        print(self.str2)

class Child(Parent1, Parent2):
    def assign_str3(self,str3):
        self.str3 =str3
    def show_str3(self):
        print(self.str3)

c1=Child()
c1.assign_str1("ulfat")
c1.assign_str2("jarin")
c1.assign_str3("richi")

print(c1.show_str1())
print(c1.show_str2())
print(c1.show_str3())


#multilevel (parent - child - grandchild)

class Parent3:
    def assign_name(self,name):
        self.name =name
    def show_name(self):
        return self.name
    
class Child(Parent3):
    def assign_age(self,age):
        self.age =age
    def show_age(self):
        return self.age
    
class Grandchild(Child):
    def assign_gender(self,gender):
        self.gender =gender
    def show_gender(self):
        return self.gender

g1=Grandchild()
g1.assign_name('ulfat')
g1.assign_age(23)
g1.assign_gender("female")

print(g1.show_name())
print(g1.show_age())
print(g1.show_gender())



