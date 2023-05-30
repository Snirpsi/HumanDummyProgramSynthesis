#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates all ports or calculates user input. """    
    while True:
        ports = find_ports()
        ports_str = ','.join(ports)
        print('Ports found: %s' % ports_str)
        
        choice = input('Choose a port (1-%s): ' % len(ports))
        if choice == '':
            break
        
        try:
            port = int(choice)
        except ValueError:
            print('Invalid port number: %s' % choice)
            continue
        
        if port < 1 or port > len(ports):
            print('Invalid port number: %s' % choice)
            continue
        
        ports[port] = choice
        
        print('Port %s is now %s' % (port, ports[port]))
        
        print('')
        
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('')
    
    print('