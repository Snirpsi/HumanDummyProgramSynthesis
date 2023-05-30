#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers or removes all ports. """    
    
    import sys
    
    ports = []
    
    for arg in sys.argv[1:]:
        if arg == '--ports':
            ports = sys.argv[2:]
            break
    
    ports = ports or []
    
    for port in ports:
        
        port_number = int(port)
        
        if port_number > 65535:
            print('Port number {} is too large.'.format(port_number))
            continue
        
        if port_number in ports:
            print('Port number {} is already in use.'.format(port_number))
            continue
        
        ports.append(port_number)
        
    print('Ports:')
    
    for port in ports:
        print('  {}'.format(port))
        
    print('Done.')
    
