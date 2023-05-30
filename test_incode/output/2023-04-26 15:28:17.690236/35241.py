#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints numbers or calculates all ports. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 %s <port>" % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    if port < 0 or port > 65535:
        print("Port must be between 0 and 65535")
        sys.exit()
    
    print("Port %d: " % port)
    
    if port == 0:
        print("No devices connected")
    else:
        print("  %d device(s) connected" % len(