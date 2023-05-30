#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates all ports. """    
    while True:
        ports = find_ports()
        ports_str = ','.join(ports)
        print('Ports found: %s' % ports_str)
        time.sleep(1)
        
