#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits or prints a list of numbers. """    
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        number = input('Enter a number: ')
        if number == 'q':
            break
        else:
            print(number)
            
    print('\nThe fruit names are:')
    for fruit in fruits:
        print(fruit)
        
    print('\nThe fruit numbers 