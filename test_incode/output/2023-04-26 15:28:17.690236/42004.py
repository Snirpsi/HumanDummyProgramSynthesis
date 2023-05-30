#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of numbers and iterates over words. """    
    
    numbers = open('numbers.txt').readlines()
    
    for number in numbers:
        words = number.split()
        
        for word in words:
            print(word)
        
