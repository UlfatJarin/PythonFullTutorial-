"""#area of circle 
pie =3.1416
radius = float(input('enter radious ='))

area_of_circle = pie * radius * radius
print(f'Area of Circle:{area_of_circle}')"""


"""# Calculater 
num1 = float(input('Enter 1st number = '))
num2 = float(input('Enter 2nd number = '))
operation = input ('Enter operation (+ ,-,*,/, // ,** ,% ) :')

while True:
    if operation == '+':
        print(num1 + num2)
    elif operation == '-':
        print(num1 - num2)
    elif operation == '*':
        print(num1 * num2)
    elif operation == '/':
        print(num1 / num2)
    elif operation == '//':
        print(num1 // num2)
    elif operation == '**':
        print(num1 ** num2)
    elif operation == '%':
        print(num1 % num2)
    else :
        print("worng operation")
    
    should_continue =input("Continue? (y/n):")
    if should_continue == "n" :  
        break
    else:
        pass"""

"""#find even number .......................
for i in range(1,11):
    if i%2 ==0 :
        print("even",i)
    else :
        print("odd",i)"""


# skip a number
start = int (input("enter start="))
stop = int (input("enter stop="))

skip= int (input('number you want to skip'))

if start < stop:
    for i in range(start ,stop):
        if i==skip:
            continue
        print(i)
else :
    print ('Invalid')






