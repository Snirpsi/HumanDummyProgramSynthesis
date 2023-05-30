#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over fruits and opens numbers. """    
    fruits = ['apple', 'banana', 'cherry']
    fruits.sort()
    
    for fruit in fruits:
        number = open_fruit(fruit)
        print(number)
        
def open_fruit(fruit):
    """ Opens a fruit and returns its number. """
    number = int(input('Enter a number: '))
    
    if fruit == 'apple':
        return number
    elif fruit == 'banana':
        return number * 2
    elif fruit == 'cherry':
        return number * 3
    else:
        print('Invalid fruit name.')
        
