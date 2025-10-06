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