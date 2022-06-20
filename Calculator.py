i = 0
while i < 1:
    num1 = int(input('Enter your first number: '))
    num2 = int(input('Enter your second number: '))
    print('\n \n Please Enter the type of operation you want to perform:')
    print(' +  for addition ')
    print(' -  for subtraction ')
    print(' *  for multiplication ')
    print(' /  for division ')
    print(' %  for modulas ')
    print(' ** for Exponjentiation ')
    print(' /  for floor \n \n ')

    oper = input()

    if oper == '+':
        print(num1, ' + ', num2, ' = ',  num1 + num2)
        print("Enter 1 to exit OR Enter 0 to continue")
        i = int(input())

    elif oper == '-':
        print(num1, ' - ', num2, ' = ',  num1 + num2)
        print(num1 - num2)
        print("Enter 1 to exit OR Enter 0 to continue")
        i = int(input())

    elif oper == '*':
        print(num1, ' * ', num2, ' = ',  num1 + num2)
        print(num1 * num2)
        print("Enter 1 to exit Enter 0 to continue")
        i = int(input())

    elif oper == '/':
        print(num1, ' / ', num2, ' = ',  num1 + num2)
        print(num1 / num2)
        print("Enter 1 to exit Enter 0 to continue")
        i = int(input())

    elif oper == '%':
        print(num1, ' % ', num2, ' = ',  num1 + num2)
        print(num1 / num2)
        print("Enter 1 to exit Enter 0 to continue")
        i = int(input())

    elif oper == '**':
        print(num1, ' ** ', num2, ' = ',  num1 + num2)
        print(num1 / num2)
        print("Enter 1 to exit Enter 0 to continue")
        i = int(input())

    elif oper == '//':
        print('{} // {} = '.format(num1, num2))
        print(num1 / num2)
        print("Enter 1 to exit Enter 0 to continue")
        i = int(input())

    else:
        print('Enter a valid operator, please run the program again.')
