#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words and removes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s words.txt' % sys.argv[0])
        sys.exit()
    
    with open(sys.argv[1]) as f:
        words = f.read().splitlines()
    
    numbers = 