#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers. """    
    import sys
    import argparse
    parser = argparse.ArgumentParser(description='Convert a list of numbers to a list of strings.')
    parser.add_argument('numbers', metavar='N', type=int, nargs='+', help='A list of numbers to convert.')
    args = parser.parse_args()
    numbers = args.numbers
    numbers = list(map(str, numbers))
    numbers = list(map(int, numbers))
    numbers = list(map(str, numbers))
    print(numbers)
    
