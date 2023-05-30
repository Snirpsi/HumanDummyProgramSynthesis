#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 remove-numbers.py <filename>")
        sys.exit()
    
    filename = sys.argv[1]
    
    with open(filename) as f:
        numbers = f.read().splitlines()
        
    numbers = [int(n) for n in numbers]
    
    with open(filename, 'w') as f:
        f.write('\n'.join(str(n) for n in numbers))
    
    print("Removed %d numbers from %s." % (len(numbers), filename))
    
