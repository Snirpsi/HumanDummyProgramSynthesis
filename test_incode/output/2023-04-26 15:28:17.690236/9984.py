#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints all ports or converts numbers. """    
    ports = [int(i) for i in sys.argv[1:]]
    ports.sort()
    
    for port in ports:
        print(port)
    
