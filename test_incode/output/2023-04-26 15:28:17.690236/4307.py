#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python {} <filename>".format(sys.argv[0]))
        sys.exit()
    
    filename = sys.argv[1]
    
    with open(filename) as f:
        lines = f.readlines()
        
    numbers = [int(line) for line in lines]
    
    numbers_as_strings = [str(number) for number in numbers]
    
    numbers_as_strings_as_ints = [int(number) for number in numbers_as_strings]
    
    numbers_as_strings_as_ints_as_strings = [str(number) for number in numbers_as_strings_as_ints]
    
    numbers_as_strings_as_ints_as_strings_as_ints = [int(number) for number in numbers_as_strings_as_ints_as_strings_as_ints]
    
    numbers_as_strings_as_ints_as_strings_as_ints_as_strings = [str(number) for number in numbers_as_strings_as_ints_as_strings_as_ints_as_strings]
    
    numbers_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints = [int(number) for number in numbers_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints]
    
    numbers_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_strings_as_ints_as_