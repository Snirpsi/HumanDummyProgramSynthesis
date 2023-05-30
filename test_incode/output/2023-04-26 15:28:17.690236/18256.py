#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates user input or multiplyes a port. """    
    
    port = int(sys.argv[1])
    
    if port < 0 or port > 65535:
        print("Invalid port number")
        
    