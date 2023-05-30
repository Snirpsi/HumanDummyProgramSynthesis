#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes fruits and returns user input. """    
    fruits = ['apple', 'banana', 'orange']
    
    fruits_multiplied = []
    
    for fruit in fruits:
        fruits_multiplied.append(int(fruit) * 5)
    
    fruits_multiplied.sort()
    
    print('The fruit multiplied is', fruits_multiplied)
    
