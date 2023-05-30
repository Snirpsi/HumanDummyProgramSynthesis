#!/usr/bin/python3
if __name__ == '__main__':
    #A function that requests user input.
    #It will ask the user to enter a number.
    #If the number is greater than 10, it will print a message.
    #If the number is less than 10, it will print a message.
    #If the number is equal to 10, it will print a message.
    #If the number is equal to 0, it will print a message.
    number = int(input('Enter a number: '))
    if number > 10:
        print('The number is greater than 10')
    elif number < 10:
        print('The number is less than 10')
    elif number == 0:
        print('The number is equal to 0')
    else:
        print('The number is equal to 10')

