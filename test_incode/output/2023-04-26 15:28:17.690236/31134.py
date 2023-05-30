#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens fruits or multiplyes a list of words. """    
    
    while True:
        fruit = input('Enter a fruit: ')
        
        if fruit == 'quit':
            break
        
        print('Fruit is', fruit)
        
        fruits = [