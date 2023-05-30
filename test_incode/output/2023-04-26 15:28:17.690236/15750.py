#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        sys.exit("usage: python remove-numbers.py <filename>")
    
    with open(sys.argv[1]) as file:
        numbers = file.read().splitlines()
    
    numbers = [x for x in numbers if x not in numbers]
    
    with open(sys.argv[1], 'w') as file:
        file.write('\n'.join(numbers))
    
