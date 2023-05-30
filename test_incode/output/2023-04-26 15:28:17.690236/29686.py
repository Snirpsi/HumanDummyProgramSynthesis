#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers and returns a list of words. """    
    
    import sys
    
    numbers = []
    for line in sys.stdin:
        numbers.append(int(line))
    
    words = []
    for number in numbers:
        words.append(str(number))
    
    print(" ".join(words))
    
