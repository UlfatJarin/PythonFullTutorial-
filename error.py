# what are error ?
'''
compile time error (missing - : or ; etc)
runtime  error  ( if 10%0 or 10/0 etc)
logical error (users mistake - need + -- provide * )
'''

"""
errors in software - bugs
removing fixing these errors - debugging

exception  ->  
     start program 
     wornning sign 
     catch and handle , program crash 

exception handling -->>
    try-except
        try -code error 3 main code
        except - if occours error then what to do

"""
"""try:
    num =int (input ("Enter a number: "))
    result = 10/num 
    print(f'result:{result}')

except ZeroDivisionError:
    print('you cannot divide with zero')

except ValueError:
    print('you cannot divide with string')"""


#finally block 
# always runs  nothing matter

"""try:
    file =open('https://www.youtube.com/watch?v=gPvYox9JIYI&t=12390s')
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not Found")

finally:
    file.close()
    print("file operation completed")"""


# nested  try- except block
try:
    num1= int (input('enter number1'))
    num2= int (input('enter number2'))

    try:
        result =num1/num2
        print(f'result :{result}')
    except ZeroDivisionError:
        print (' You cannot divide with zero ')

except ValueError:
    print('you must provide a valid input')


# check possword strength
def check_password(password):
    if len(password)<8:
        raise Exception("Error: Password must be >=8 characters")
    print("password is strong")

try:
    password = input('Enter a password=')
    check_password(password)
except Exception as e :
    print(e)







