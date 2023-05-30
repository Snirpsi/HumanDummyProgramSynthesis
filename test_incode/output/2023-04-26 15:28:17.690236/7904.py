#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes fruits and multiplyes numbers. """    
    fruits = ['apple', 'banana', 'cherry', 'orange', 'mango']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    for fruit in fruits:
        for number in numbers:
            print('{} * {} = {}'.format(fruit, number, fruit*number))
    
