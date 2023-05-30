#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds user input and returns a list of numbers. """    
    
    numbers = []
    
    while True:
        number = input('Enter a number: ')
        numbers.append(int(number))
        
        if number == 'q':
            break
        
    print('\n'.join(map(str, numbers)))
    
