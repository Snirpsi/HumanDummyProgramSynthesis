#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        
        print("Adding port {}".format(port))
        
        