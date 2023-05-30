#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds numbers. """    
    import sys
    
    if len(sys.argv) != 2:
        sys.exit("Usage: python add_numbers.py <numbers>")
    
    numbers = map(int, sys.argv[1].split(","))
    
    for number in numbers:
        sys.stdout.write(str(number) + ",")
    
    sys.stdout.write("\n")