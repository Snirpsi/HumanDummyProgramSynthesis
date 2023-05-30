#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over words or multiplyes a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        
        for word in sys.argv[2:]:
            print(word * port)
    else:
        print("Usage: %s <port>" % sys.argv[0])
        
