#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over fruits and calculates all ports. """    
    
    ports = []
    
    for fruit in ['apple', 'orange', 'banana', 'cherry']:
        ports.append(get_port(fruit))
        
    print('\n'.join(ports))
    
