#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns user input and iterates over fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        fruit = get_input()
        if fruit == 'quit':
            break
        else:
            print(fruit)
            
