#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints fruits and iterates over user input. """    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    
    while True:
        fruit = input('Enter a fruit: ')
        if fruit == 'quit':
            break
        else:
            print('The fruit is', fruit)
            
    print('The program has ended.')
    
