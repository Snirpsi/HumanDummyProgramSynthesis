#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a list of numbers or adds a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python list.py <port>", file=sys.stderr)
        sys.exit(1)
    
    port = int(sys.argv[1])
    
    ports = [port]
    
    for i in range(2, len(sys.argv)):
        ports.append(int(sys.argv[i]))
    
    print(ports)
    
