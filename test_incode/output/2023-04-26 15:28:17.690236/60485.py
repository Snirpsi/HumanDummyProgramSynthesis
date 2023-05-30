#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers or removes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <numbers>" % sys.argv[0])
        sys.exit()
    
    numbers = sys.argv[1:]
    
    numbers_as_ints = [int(x) for x in numbers]
    
    numbers_as_ints_as_strings = [str(x) for x in numbers_as_ints]
    
    numbers_as_ints_as_strings_as_ints = [int(x) for x in numbers_as_ints_as_strings]
    
    numbers_as_ints_as_strings_as_ints_as_strings = [int(x) for x in numbers_as_ints_as_strings_as_ints]
    
    numbers_as_ints_as_strings_as_ints_as_strings_as_ints = [int(x) for x in numbers_as_ints_as_strings_as_ints_as_strings]
    
    numbers_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings = [int(x) for x in numbers_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings]
    
    numbers_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings = [int(x) for x in numbers_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings]
    
    numbers_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_