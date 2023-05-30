#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over user input and adds numbers. """    
    while True:
        number = int(input('Enter a number: '))
        print(number)
        
        if number == 999:
            print('Thank you for playing!')
            break
        
        