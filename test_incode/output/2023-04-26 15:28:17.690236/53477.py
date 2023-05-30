#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers and calculates words. """    
    
    numbers = range(1,10)
    words = [ "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]
    
    for number in numbers:
        word = words[number-1]
        print(number, word)
    
