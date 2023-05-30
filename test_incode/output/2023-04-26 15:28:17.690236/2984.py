#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of numbers and iterates over words. """    
    numbers = open('numbers.txt')
    words = open('words.txt')
    
    numbers = numbers.readlines()
    words = words.readlines()
    
    numbers = [int(n) for n in numbers]
    words = [w.strip() for w in words]
    
    for number in numbers:
        for word in words:
            if number == word:
                