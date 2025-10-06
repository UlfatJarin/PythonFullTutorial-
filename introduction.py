#variable ...............................................
# variable store data 
# variable = data
# no special symbol 
# no number in start 

name = 'ulfat'
age = 23
height = 5.7
print (name ,age , height)


# comments.....................................
# #- for single line comment 
'''
this is multiline comment 
'''

"""
this is also multiline comment 
"""

#Data type .................................................
"""
numeric type 
int - 1, 23,  46566,  -34
float - 1.43, -3.343
complex - real & imaginary part 
          a+bj = 3+ 4j 
"""
a = 10
b = 10.29
c= 3+4j
print (a,b,c)
print (type(a),type(b),type(c))

"""
boolian type  = True , False
logical operation
"""
"""
none type 
"""
result = None
print(result)

#sequences type .........................................
"""
1- string 
2 -list
3- tuple
"""
"""
sting ..................................................................................................
immutable - not changeable
indexed
itarable
text = "this is string" ,'is string '
for multiple line = 
"""
str = "python"
print(str[0])
print(str[-1])
print(len(str))
#slicing -  string[start:stop:step]
text = "this is pyhon the king of AI"
print(text[1:8:2])

print ("king" in text)
print ("king" not in text)

num1 ="10"
num2 ="20"
print (num1 * 3)
print(num1+num2)

str1="this IS, PYthon"
print(str1.lower())
print(str1.upper())
print(str1.capitalize()) # 1st alphabet capitalize
print(str1.title())     # every words 1st alphabet capitalize
print(str1.swapcase())  # revers uppercase = lowarcase ,, lowewrcase = uppercase 
print(str1.find("IS"))   # find index number 
print(str1.replace("PYthon","java"))   
print(str1.split(","))   # "," hisabe alada kora hoy
s = str1.split(",")      # "," hisabe alada kora hoy
print ("after splitting", s)
result = ",".join(s)  #alada kora string re join korte
print(result)
print (str1.startswith('t')) # t die start ki na 
print (str1.endswith('a'))   # a die end ki na
print(str1.isalpha()) # is all alphabetic 
print(str1.isdigit()) # is all digit 
print(str1.isalnum()) # is it mix alphabet+digit

"""
list .......................................................................................................
orderd
mulable
dynamic
netrogeneous

list=['data1' , 'data2' ,'data3']
canbe change 
"""
name ="ulfat"
age = 23
marks =89.79

my_list =[1 ,2,5,7,"hello", True]
my_list1 =((1 ,2,5,7,"hello", True))
print(my_list)
print(my_list1)

my_list[1] ='ulfat'
print(my_list)
my_list[0:3] ='ulfat','jarin' ,'richi'
print(my_list)
#concatination
lst1 =[1,2,3,4]
lst2 =[5,6,7,8]
result =lst1 +lst2
print(result)
#repitation
print(lst1*5)
#membership
check=int (input('enter a number to check='))
if check in lst1:
   print("Found")
else:
   print("not found")
#copy
lst_1 =[1,2,3]      # lst_1 = lst_2 .... memory location same
lst_2 =lst_1.copy() #copy korbe ... memory location alada
lst_2[1] =100
print(lst_1,lst_2) 

#append
a=[1,2,3]
a.append(4)  # sas a 4 add hobe
print(a)  

#extend
b=[4,5,6]
a.extend(b) # b ar element a te store hobe
print(a)

#insert
a.insert(1,"hi") # index ar value change 
print (a)

#remove
a=[1,2,3]
a.remove(3) # 3 is data not index
print (a)

#pop
a=[1,2,3]
popped = a.pop(0) #index number
print(popped)

#clear
a=[1,2,3]
a.clear() # all element clear kore dibe2
print(a)

#index
a=[1,2,3,4,5,6,7]
index = a.index(5) # data to index
print(index)

#count 
a=[1,2,3,4,5,1,1,3,4,1,1,"python", "Java",True]
counter = a.count(1) # how many 1 is present
print(counter)

#sort
a=[3,58,21,78,16,-66,99,48,19,5,30,-39]
a.sort()
print(a)

#reverse
a=[1,2,3]
a.reverse()
print(a)

#copy

#minimum &maximum
a=[3,58,21,78,16,-66,99,48,19,5,30,-39]
print(min(a))
print(max(a))

# set - common element
a=[1,2,3]
b=[3,4,5]

s1=set(a)
s2=set(b)

s3 = s1.intersection(s2)
print(list(s3))

#nested list
a=[1,2,3,4]
b=[4,5,6,7,[9,10,11]]


#list with range
number = list(range(1,11,1))
print (number)

#listcompre
'''
[expression for item in iterable if condition]

e - x*2
item -
iterable - range(1,11)
condition -optional
'''
squares=[]
for i in range(1,11):
   squares.append(i ** 2)
print(squares)

squares =[i**2 for i in range(1,11) if i%2 == 0]
print(squares)



"""
tuple ...............................................................................................
immutable
hetrogenious
like list but use ()
tuple = ('data1' , 'data2' ,'data3')
cannot change 
only for read
"""
a=(10,20,30)
b=()
print(type(a))
print(type(b))

#len()
#min & max
#count()
#sorted()
#index()


"""
set  -{}
unique
mutable 
   can be modify 
immutable 
   cannot be modify 
"""


"""
dictionary -{}....................................................................................
unorderd3.7 , ordered
mutable
dynamic
pair (key : value)
key is unique
key: value key1:value1
"""
my_dic ={ "name": "ulfat" ,"age" :23 , "Marks" :{89,79,99,79} ,100:"abc"}
print(my_dic)

dic1 = {"Fruites":['Banana','Apple','orange'], 'Category':"fruit"}
print(dic1)
# add element
dic1['price']=1000
print(dic1)
# update element
dic1['Category']='flower'
print(dic1)
#delete element 
del dic1["Category"]
print(dic1)

## method

profile ={'name':'Jarin','age':'23','salary':25000.00}

#get
age = profile.get('age','not found')
print(age)
age2 = profile.get('age2','not found')
print(age2)

#keys
keys= profile.keys()
print(list(keys))

#values
values= profile.values()
print(list(values))

#items
all_items = profile.items()
print(list(all_items))

#pop
popped = profile.pop('age_2','not found')
popped1= profile.pop('age','not found')
print(popped)
print(popped1)
print(profile)

#popitem  
popped_i = profile.popitem() #last item will be deleted
print(popped_i)
print(profile)

#clear
cleared =profile.clear() #all iem will be deleted
print(profile)

# dictionary_com
squares = {x : x*x for x in range(1,6)}
print(squares)

#nested dic 
progemming_language={
    "python":{'name ':'python' , 'use_case':['ai,ml,webdev,ds']},
    "java":{"name":'python',"use_case":['app dev']}
}
print(progemming_language)

# in for loop
for k in profile.items():
    print (k)
    


#Oparators..............................................................
"""
BODMOS

PEMDAS
perntjesis ()
exponent **
multipication & divition  *, //, /,%
addition & substaction + ,-

"""
result = 10 + 5* 2
print (result)
result1 =25/10
print (result1)
result2 =25//10
print (result2)

#Arithmathic oparator ...........................................
x=10
y=20

print (x+y)
print (x-y)
print (x*y)
print (x/y) #division
print (x//y)#floor division
print (x%y) #modulus - remainer
print (x**y)# power 10^20

#comparison operater..................................................
#compare values - return True or False
x=10
y=5

print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)


#logical operater ....................................
"""
multiple condition combine

and - all true > True
or  - one true > True
not - reverse
"""
"""age =20
is_student = True

print(age>18 and is_student)
print(age>25 or is_student)
print(not is_student)"""

a=10
b=20
print(a>5 and b>10)
print(a<1 or b==20)
print(not(a==10))

# assignment Operater..............................................
"""
=
+= (x *= 5)
-=
*=
"""

#identity operator................................................
'''
check memory location
is - True 
is not - True 
'''
a =[1,2,3]
b =a
c= [1,2,3]

print(a is b)
print(a is c)
print(a is not b)

#membership operater....................................
'''
check value existance
in - True 
not in - True 
'''
vegetables =['Karela','Aloo','Tomato']
print('Bhendi' in vegetables)
print('Tomato' in vegetables)




#.....................................................................
#..................................................................... 
#control statement 
"""
conditional statement - if 
                      - if else
                      - if elif else

"""
"""
loops - while loop
      - for loop
---------------------------
while loop 
while condition:
    execution 
----------------------------
for a in list 

"""

a=[1,2,3,4,5,]
for i in a :
    print(i)
    


#Range fanction .......................................
"""
range (start ,stop) by defult step =1
range(start, stop ,step)

start -1
stop - 100, exclude means - if 10 then its mean 9 
                            if 100 then   99
step - 2 , means how many gap  - for 1 - 1,2,3,4,...
                                 for 2 - 1,3,5,7,...
"""
a= list(range(1, 10 ,1))
b= list(range(1, 10 ,2))
print (a)
print (b)

#nested loop .............................................
for i in range(1,3):
    for j in range(3,6):
        print (f'{i},{j}')

#break ...................................................
#continue ................................................
 # for skip 
# pass....................................................
 # jemon ache tamon cholbe ... pore change korte chily kora jabe
#  







