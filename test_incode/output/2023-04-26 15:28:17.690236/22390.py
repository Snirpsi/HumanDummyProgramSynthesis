#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words or multiplyes fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        print('\n'.join([f'{fruits[i]} * {fruits[i+1]}' for i in range(0, len(fruits)-1)]))
        
