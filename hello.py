print("hello world!!")



#list 

li = [1, "sparta", 3.14 , True , 3+5j ]
print ( li [-1])

print ( li [1:4])

li[0] = 100
print ( li)

li.append("ulfat") 
print ( li)

li.pop() 
print ( li)

li.reverse()
print(li)

li.reverse()
print(li)

li.insert(1,"ulfat")
print(li)

li.insert(2,5)
print(li)

li2=["red" ,"orange","yellow","green","brown","blue"]
li2.sort()
print(li2)

print(li + li2)
print(li*3)

#dictionary

fruit = {'apple':50 , 'banana':30,'orange':40, 'peach':100 }
print(type(fruit))

print(fruit.keys())
print(fruit.values())

fruit["guava"]=20
print(fruit)

fruit["apple"]=60
print(fruit)

fruit.pop('orange')
print(fruit)

color1={'red':111 , 'blue':222}
color2={'green':333 , 'brown':444}
color1.update(color2)
print(color1)


#set

s1 = {1,2,3,"ulfat","jarin", 2,5,3}
print(s1) #dupticate not allowed

s1.add('True') # add 1 element
print(s1)

s1.update([ 10,6]) #add multiple elements
print(s1)

s1.remove('True')
print(s1)

st1 ={1,2,3}
st2 ={"a","b","c"}
print(st1.union(st2))

st1 ={1,2,3 ,7 ,4, 'b' ,'d,.'}
st2 ={"a","b","c" ,7 ,1}
print(st1.intersection(st2))

#if statement
a=10
b=20
c=30

if a>b:
    print(" a is greater than b")
else: 
    print("b is greater than a")   


if (a>b & a>c):
    print(" a is greatesst ")
elif(b>a & b>c): 
    print("b is greatest")   
else:
    print("c is greatest") 

tup1= (1,2,3,4)
if 2 in tup1:
    print("2 is present in the tuple")
else: 
    print("2 is not present")

if 5 in tup1:
    print("5 is present in the tuple")
else:
    print("5 is not present")

#if with list 
l1=[1,2,3,4,5]
if l1[1]==2:
    l1[1] = l1[1]+100
    print(l1)

#     for loop 

l1=["apple" , "banana" , "orange"]
for i in l1:
    print (i)

l2= ['red',"yellow","orange"]
for i in l1:
    for j in l2:
        print (i,j)

#python function.........................................................................

def hello():
    print("Hello world")

hello()


def add10(x):
    print(x +100)

add10(10)


#lamda function

g = lambda x: x*x*x
print(g(7))  
print(g(6))

# lamda with filter
li =[5,7,22,97,54,62,77,23,73,61]
odd_number = list(filter(lambda x:(x%2 !=0), li))

print(odd_number)
print(list(filter(lambda x:(x%2 !=0), li)))

# lamda function with map
li =[5,7,22,97,54,62,77,23,73,61]
multiple_number=list(map(lambda x:x*2 ,li))

print(multiple_number)

#lambda with import reduce
from functools import reduce
li =[ 5,8,10,20,50,100]
sum = reduce((lambda x,y : x+ y),li)
print(sum)


