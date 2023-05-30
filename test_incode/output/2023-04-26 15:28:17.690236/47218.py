#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over words and stores a list of numbers. """    
    words = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
    numbers = []
    for word in words:
        numbers.append(int(word))
    print(numbers)
    
