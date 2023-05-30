#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers or returns a list of words. """    
    import sys
    
    if len(sys.argv) == 1:
        numbers = open('numbers.txt').read().splitlines()
    else:
        numbers = sys.argv[1:]
    
    for number in numbers:
        print(number)
    
