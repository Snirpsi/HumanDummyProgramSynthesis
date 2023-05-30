#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores fruits and adds a list of numbers. """    
    fruits = ['apple', 'banana', 'cherry']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    while True:
        print('The fruit is', fruits.pop())
        print('The number is', numbers.pop())
        
