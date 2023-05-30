#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers and calculates a list of words. """    
    
    numbers = [int(n) for n in sys.argv[1:]]
    
    words = []
    for n in numbers:
        words.append(str(n) + 