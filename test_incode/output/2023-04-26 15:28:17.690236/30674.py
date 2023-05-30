#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes fruits or removes a list of numbers. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        
        fruit = input('What would you like to remove? ')
        
        if fruit == 'quit':
            break
        
        if fruit in fruits:
            fruits.remove(fruit)
            
        else:
            print('That fruit does not exist!')
            
    print('The fruit list has 