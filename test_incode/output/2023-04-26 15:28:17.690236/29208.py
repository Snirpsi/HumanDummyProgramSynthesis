#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes all ports or iterates over fruits. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        fruit = input('Enter fruit name: ')
        if fruit in fruits:
            fruits.remove(fruit)
        else:
            print('No fruit found')
            break
        
    print('Done')
