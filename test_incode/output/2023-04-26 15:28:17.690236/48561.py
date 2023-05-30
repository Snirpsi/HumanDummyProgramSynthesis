#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers and converts numbers. """    
    import sys
    numbers = sys.argv[1:]
    numbers = [int(n) for n in numbers]
    numbers = [n for n in numbers if n not in range(10)]
    print(numbers)
    
<|/ file filename=