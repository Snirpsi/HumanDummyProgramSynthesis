#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers or converts user input. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <list>" % sys.argv[0])
        sys.exit()
    
    list