#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a port. """    
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 ports.py <port>")
        sys.exit()
    port = sys.argv[1]
    print("Port: {}".format(port))
    
