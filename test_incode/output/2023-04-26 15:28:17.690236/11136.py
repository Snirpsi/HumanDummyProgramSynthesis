#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
        
        print("Adding port {}".format(port))
        
        