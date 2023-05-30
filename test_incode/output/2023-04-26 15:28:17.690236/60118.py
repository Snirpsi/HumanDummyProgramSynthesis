#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints user input or enumerates fruits. """    
    
    fruits = ['apple', 'banana', 'orange']
    
    while True:
        fruit = input('Enter a fruit: ')
        if fruit in fruits:
            print(fruit)
        else:
            print('Invalid fruit')
            
