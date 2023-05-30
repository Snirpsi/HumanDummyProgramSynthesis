#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates numbers. """    
    
    # Read in input from STDIN
    line = sys.stdin.readline()
    
    # Convert input from string to float
    number = float(line)
    
    # Print result
    print(number)
    
    # Close STDIN
    sys.stdin.close()
    
    # Close STDOUT
    sys.stdout.close()
    
    # Close STDERR
    sys.stderr.close()
    
    # Close all open files
    sys.stdout.close()
    sys.stderr.close()
    
    # Exit program
    sys.exit(0)
    
