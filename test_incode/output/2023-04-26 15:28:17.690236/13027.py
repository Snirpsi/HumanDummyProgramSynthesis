#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python storeport.py <port>")
        sys.exit()
    
    port = sys.argv[1]
    
    storeport(port)
    
    print("Port stored successfully.")
    
