#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates fruits. """    
    while True:
        fruits = input('Enter fruits: ')
        if fruits == 'quit':
            break
        else:
            fruits = fruits.split()
            fruits = [fruit.upper() for fruit in fruits]
            fruits.sort()
            print(' '.join(fruits))
            
