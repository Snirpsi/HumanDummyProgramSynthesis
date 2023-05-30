#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a list of numbers or returns a list of words. """    
    import sys
    
    numbers = [int(i) for i in sys.argv[1:]]
    
    words = []
    
    for number in numbers:
        words.append(str(number))
    
    print(words)
    
