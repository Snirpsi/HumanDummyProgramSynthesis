#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over numbers and enumerates fruits. """    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    fruits = ['apple', 'banana', 'orange', 'kiwi', 'grape', 'pear', 'pineapple', 'plum']
    
    for number, fruit in zip(numbers, fruits):
        print("{} is {} {}".format(number, fruit, 