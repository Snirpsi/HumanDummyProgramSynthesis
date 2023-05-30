#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port or converts numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 1
    
    for port in range(1,65535):
        print(port)
        
    if port == 1:
        print("Port 1 was found")
    else:
        print("Port %d was found