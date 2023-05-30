#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python enumerate.py <file>')
        sys.exit()
    
    with open(sys.argv[1]) as f:
        for line in f:
            print(line)
    
