#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes all ports. """    
    ports = [int(i) for i in sys.argv[1].split(',')]
    
    ports_out = []
    
    for port in ports:
        ports_out.append(port * 2)
    
    print(ports_out)
    
    
