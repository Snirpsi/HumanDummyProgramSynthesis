#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates all ports. """    
    
    ports = []
    
    for port in os.listdir('/sys/class/net/'):
        
        if port.startswith('eth'):
            
            ports.append(port)
            
    print('\n'.join(ports))
    
