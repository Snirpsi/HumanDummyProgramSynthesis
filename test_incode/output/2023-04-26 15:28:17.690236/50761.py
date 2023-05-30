#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints fruits or adds a list of numbers. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        fruit = input('What would you like to eat? ')
        if fruit == 'quit':
            break
        elif fruit not in fruits:
            print('That is not a valid fruit!')
        else:
            print('You eat ' + fruit)
            
    print('Thank you for playing!')
    
