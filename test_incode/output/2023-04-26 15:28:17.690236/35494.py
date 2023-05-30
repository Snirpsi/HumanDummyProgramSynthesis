#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens numbers and prints user input. """    
    while True:
        number = int(input('Enter a number: '))
        if number > 10:
            print('Too high')
        elif number < 10:
            print('Too low')
        else:
            print(number)
            break
