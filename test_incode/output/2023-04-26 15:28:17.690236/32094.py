#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts all ports or multiplyes numbers. """    
    ports = sys.argv[1:]
    ports = ports.split(',')
    ports = [int(p) for p in ports]
    ports = ports * len(ports)
    
    for p in ports:
        print(p)
        
