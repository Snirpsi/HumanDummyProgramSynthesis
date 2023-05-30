#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores user input and enumerates fruits. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        
        fruit = input('Enter a fruit: ')
        
        if fruit in fruits:
            print('You entered a fruit!')
        else:
            print('You entered a non-fruit!')
            
