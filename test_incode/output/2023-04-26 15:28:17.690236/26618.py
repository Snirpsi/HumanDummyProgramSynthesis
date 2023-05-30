#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <list>" % sys.argv[0])
        sys.exit()
    
    numbers = sys.argv[1:]
    
    numbers_as_strings = [str(number) for number in numbers]
    
    numbers_as_strings_as_ints = [int(number) for number in numbers_as_strings]
    
    numbers_as_strings_as_ints_as_floats = [float(number) for number in numbers_as_strings_as_ints]
    
    numbers_as_strings_as_ints_as_floats_as_strings = [str(number) for number in numbers_as_strings_as_ints_as_floats]
    
    numbers_as_strings_as_ints_as_floats_as_strings_as_ints = [int(number) for number in numbers_as_strings_as_ints_as_floats_as_strings_as_ints]
    
    numbers_as_strings_as_ints_as_floats_as_strings_as_ints_as_floats = [float(number) for number in numbers_as_strings_as_ints_as_floats_as_strings_as_ints_as_floats]
    
    numbers_as_strings_as_ints_as_floats_as_strings_as_ints_as_floats_as_strings = [str(number) for number in numbers_as_strings_as_ints_as_floats_as_strings_as_ints_as_floats_as_strings]
    
    numbers_as_strings_as_ints_as_floats_as_strings_as_ints_as_floats_as_strings_as_ints_as_floats = [int(number) for number in numbers_as_strings_as_ints_as_floats_as_strings_as_ints_as_floats_as_strings_as_ints_as_floats]
    
    numbers_as_strings_as_ints_as_floats_as_strings_as_ints_as_floats_as_strings_as_ints_as_floats_as_strings_as_ints_as_floats = [float(number) for number in numbers_as_strings_as_ints_as_floats_as_strings_as_ints_as_floats_as_strings_as_ints_as_floats_as_strings_as_ints_as_floats]
    
    numbers_as_strings_as_ints_as_floats_as_strings_as_ints_as_floats_as_strings_as_ints_as_floats_as_strings_as_ints_as_floats_as_strings_as_ints_as_floats = [str(number) for number in numbers_as_strings_as_ints_as_floats_as_strings_as_ints_as_floats_as_strings_as_ints_