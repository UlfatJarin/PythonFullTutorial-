# reuseability
# modularity
# scoping
# maintanance

"""
function meaning
length of functions
avoid global variables
    -

"""

#perameter  - 
# & argumnet  -
"""
 def function_name( perameter):
       work + display

 function_name( argumnet)   # function call
 """
 
def greet(name):
    print("Hii!",name)

greet("ulfat")
greet("jarin")
greet("richi")

#positional argumnet - position wise data pass 
def greet2(name ,city):
    print(f'Welcome {name} to the {city}')

greet2( 'Jarin' , 'Dubai')

#keyword argumnet 
def greet2(name ,city):
    print(f'Welcome {name} to the {city}')

greet2( name='Jarin' , city='Dubai')

#defult argumnet
def greet2(name='Richi' ,city='Mumbai'):
    print(f'Welcome {name} to the {city}')

greet2()
greet2( name='Jarin' , city='Dubai')
greet2( 'Jarin' , 'Dubai')

#return state 
def greet2(name ,city):
    print(f'Welcome {name} to the {city}')
    return name           
greet2( 'Jarin' , 'Dubai')
return_value = greet2( 'Jarin' , 'Dubai')
print(return_value)

 
 
 #decorator
"""
burger - function
extra cheese -extra feature
main funtion > function add
without changeing the main function code
"""

def my_decorator(func):
    def wrapper():
        print("before function call")
        func()
        print("after function call")
    return wrapper

@my_decorator
def say_hello():
    print("hello")

say_hello()


#genarator 
def count_down (num):
    while num > 0:
        yield num    #yeild values one at a time 
        num -=1

#using genartor
for number in count_down(5):
    print(number)



#lambda function / annomonus function
# lambda argument : experssion condition      #only one expression
add_ten =lambda x:x+10
print(add_ten(5))







