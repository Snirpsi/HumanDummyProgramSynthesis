#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a port or prints numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        
        if port > 0 and port < 65535:
            print(port)
        else:
            print("Invalid port number")
    else:
        print("Usage: python port_number.py <port number>")
        
