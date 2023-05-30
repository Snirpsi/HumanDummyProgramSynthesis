#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a list of numbers and iterates over user input. """    
    
    numbers = []
    
    while True:
        number = input('Enter a number: ')
        numbers.append(number)
        
        if number == 'q':
            break
        
    print('The numbers 