#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a port or returns user input. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    if port < 0 or port > 65535:
        print("Invalid port number")
    else:
        print("Port number " + str(port))
    
