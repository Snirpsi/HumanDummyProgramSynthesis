#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words and stores a list of numbers. """    
    
    import sys
    
    words = []
    numbers = []
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
        
    if len(sys.argv) > 2:
        numbers = sys.argv[2:]
    
    numbers_str = ""
    
    for number in numbers:
        numbers_str += str(number) + " "
    
    numbers_str = numbers_str[:-1]
    
    word