#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints all ports or stores all ports. """    
    
    import sys
    
    if len(sys.argv) > 1:
        ports = sys.argv[1:]
    else:
        ports = range(1024)
    
    for port in ports:
        print('Port %d' % port)
    
