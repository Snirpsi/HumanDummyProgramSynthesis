#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over numbers and multiplyes a list of words. """    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    
    for number in numbers:
        for word in words:
            print(number * word)
