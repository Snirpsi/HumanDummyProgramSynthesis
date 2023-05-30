#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a port or removes a list of numbers. """    
    
    ports = sys.argv[1:]
    
    if len(ports) == 0:
        print('Usage: %s [port]' % sys.argv[0])
        sys.exit()
    
    for port in ports:
        if port == '-':
            ports = ports.