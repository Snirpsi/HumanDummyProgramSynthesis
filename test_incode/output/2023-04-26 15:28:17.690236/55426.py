#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits and opens fruits. """    
    
    fruits = open('fruits.txt', 'r')
    
    fruits.readline()
    
    while True:
        fruit = fruits.readline()
        
        if fruit == '':
            break
        
        print('