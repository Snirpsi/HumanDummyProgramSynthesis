#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints user input. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <filename>" % sys.argv[0])
        sys.exit()
    
    filename = sys.argv[1]
    
    with open(filename) as fp:
        for line in fp:
            print(line)
    
