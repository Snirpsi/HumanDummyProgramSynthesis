#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words and multiplyes a list of numbers. """    
    
    import sys
    
    words_to_remove = sys.argv[1]
    
    numbers_to_multiply = sys.argv[2]
    
    numbers_to_multiply = list(map(int, numbers_to_multiply))
    
    numbers_to_multiply = list(map(lambda n: n * numbers_to_remove, numbers_to_multiply))
    
    print(numbers_to_multiply)
    
