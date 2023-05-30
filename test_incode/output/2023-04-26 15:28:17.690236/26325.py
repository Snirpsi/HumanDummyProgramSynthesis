#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of numbers or multiplyes words. """    
    
    while True:
        line = input('Enter a number: ')
        try:
            number = int(line)
        except ValueError:
            print('Invalid input.')
            continue
        
        if number < 0:
            print('Negative number.')
            continue
        
        if number == 0:
            break
        
        print('The number multiplied by {} is {}.'.format(number, number * number))
        
        print('Press enter to exit.')
        
        input()
        
    print('Goodbye.')
    
