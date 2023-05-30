#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of numbers and multiplyes numbers. """    
    numbers = openFile('numbers.txt')
    numbers = multiplyNumbers(numbers)
    writeFile('numbers.txt', numbers)
    
