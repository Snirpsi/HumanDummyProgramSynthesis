#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers and returns fruits. """    
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    fruits = []
    
    for number in numbers:
        fruits.append(number)
        
    print('\n'.join(str(number) for number in fruits))
    
