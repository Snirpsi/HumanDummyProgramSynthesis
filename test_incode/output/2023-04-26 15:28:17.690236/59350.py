#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates all ports or removes a list of numbers. """    
    ports = [int(i) for i in sys.argv[1:]]
    
    if len(sys.argv) > 2:
        ports.remove(int(sys.argv[2]))
    
    ports = list(set(ports))
    
    for port in ports:
        print('Port #{}'.format(port))
    
