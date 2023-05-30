#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a port. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python multiply_port.py <port>")
        exit(1)
    
    port = int(sys.argv[1])
    
    print("Multiplying port {} by {}".format(port, port * 2))
    
