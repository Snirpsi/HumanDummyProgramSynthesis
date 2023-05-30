#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores numbers. """    
    
    numbers = []
    
    while True:
        number = int(input('Enter a number: '))
        numbers.append(number)
        
        if number == -1:
            break
    
    print('The numbers 