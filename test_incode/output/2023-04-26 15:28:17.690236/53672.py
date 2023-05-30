#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates fruits or opens user input. """    
    
    fruits = ['apple', 'banana', 'orange', 'kiwi']
    
    while True:
        fruit = input('Enter a fruit: ')
        if fruit in fruits:
            print('You entered ' + fruit)
        else:
            print('Sorry, I did not recognize that fruit.')
            
