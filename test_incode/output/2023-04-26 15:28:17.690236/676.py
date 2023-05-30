#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over fruits and iterates over numbers. """    
    fruits = ['apple', 'banana', 'cherry']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    for fruit in fruits:
        for number in numbers:
            print('{} {}'.format(fruit, number))
    
    print('Done!')
    
