#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a port. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python remove-port.py <port>")
        exit()
    
    port = sys.argv[1]
    
    print("Removing port %s..." % port)
    
    subprocess.call(["iptables", "-D", "INPUT", "-p", port, "-o", "