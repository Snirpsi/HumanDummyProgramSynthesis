#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates words or removes all ports. """    
    
    # Read input from stdin
    lines = sys.stdin.readlines()
    
    # Remove all ports
    lines = removePorts(lines)
    
    # Write output to stdout
    sys.stdout.write('\n'.join(lines))
    
