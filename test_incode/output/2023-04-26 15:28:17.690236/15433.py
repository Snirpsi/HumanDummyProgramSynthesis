#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens numbers. """    
    numbers = open('numbers.txt', 'r')
    numbers_string = numbers.read()
    numbers.close()
    print(numbers_string)
