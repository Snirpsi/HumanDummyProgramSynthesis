#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores numbers. """    
    
    # Read input from STDIN
    numbers = []
    for line in sys.stdin:
        numbers.append(int(line))
    
    # Write output to STDOUT
    sys.stdout.write('\n'.join(map(str, numbers)))
    
    # Exit with return code 0
    sys.exit(0)
    
