#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns fruits and iterates over fruits. """    
    fruits = []
    
    while True:
        fruits.append(input('Enter a fruit: '))
        
        if len(fruits) == 0:
            break
        
    print('\nThe fruits:')
    for fruit in fruits:
        print(