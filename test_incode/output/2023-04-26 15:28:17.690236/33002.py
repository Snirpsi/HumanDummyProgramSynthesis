#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes all ports. """    
    ports = [int(i) for i in sys.argv[1:]]
    
    ports_sum = sum(ports)
    
    for port in ports:
        
        port_sum = port * ports_sum
        
        print('Port {} is {} and equals {}'.format(port, port_sum, port_sum == port))
        
