#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates fruits and adds user input. """    
    while True:
        fruit = input('Enter a fruit: ')
        fruits.append(fruit)
        print('Added fruit:', fruit)
        
        if fruit == 'quit':
            break
        
    print('Fruit 