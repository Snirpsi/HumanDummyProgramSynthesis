#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds user input. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <username>" % sys.argv[0])
        sys.exit()
    
    username = sys.argv[1]
    
    print("Hello, %s" % username)
    
