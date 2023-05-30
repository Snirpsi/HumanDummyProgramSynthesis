#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words and converts a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit()
    
    words = [w.strip() for w in sys.argv[1].split(',')]
    
    numbers = map(int, sys.argv[2:])
    
    numbers_as_strings = map(str, numbers)
    
    numbers_as_strings_as_ints = map(int, numbers_as_strings)
    
    numbers_as_strings_as_ints_as_strings = map(str, numbers_as_strings_as_ints)
    
    numbers_as_strings_as_ints_as_strings_as_ints = map(int, numbers_as_strings_as_ints_as_strings)
    
    numbers_as_strings_as_ints_as_strings_as_ints_as_strings = map(str, numbers_as_strings_as_ints_as_strings_as_ints_as_strings)
    
    numbers_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints = map(int, numbers_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints)
    
    numbers_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings = map(str, numbers_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings)
    
    numbers_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings = map(int, numbers_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings)
    
    numbers_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings = map(int, numbers_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings)
    
    numbers_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings = map(int, numbers_as_strings_as_ints_as_strings_as_ints_