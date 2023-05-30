#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns fruits or calculates numbers. """    
    fruits = ['apple', 'banana', 'cherry']
    numbers = [2, 3, 4]
    
    for fruit in fruits:
        print('The fruit ' + fruit + ' is ' + fruit + ' ' + fruits[fruit] + '.')
        
    for number in numbers:
        print('The number ' + number + ' is ' + str(number) + ' times ' + numbers[number] + '.')
    
