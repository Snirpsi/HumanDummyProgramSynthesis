#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python calc_numbers.py <filename>")
        exit()
    
    filename = sys.argv[1]
    
    with open(filename) as f:
        numbers = f.read().splitlines()
    
    numbers = [int(n) for n in numbers]
    
    print(sum(numbers))
    
