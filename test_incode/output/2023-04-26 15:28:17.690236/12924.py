#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input and stores a list of numbers. """    
    
    while True:
        number = input('Enter a number: ')
        numbers.append(number)
        
        if number == 'done':
            break
        
        print('Number added:', number)
        
    print('Done!')
    
    print('The numbers 