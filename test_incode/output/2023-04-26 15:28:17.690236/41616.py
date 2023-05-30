#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes numbers and multiplyes fruits. """    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    numbers = [1, 2, 3, 4]
    
    for fruit in fruits:
        for number in numbers:
            print('{} * {} = {}'.format(fruit, number, fruit*number))
            
