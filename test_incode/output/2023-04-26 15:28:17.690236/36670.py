#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds user input and adds all ports. """    
    
    ports = []
    
    while True:
        port = input('Enter a port number: ')
        ports.append(port)
        
        if port == 'q':
            break
    
    for port in ports:
        ports.append(port)
    
    for port in ports:
        print('Adding port number {} to port list'.format(port))
        
        ports.append(port)
        
    print('Ports added')
    
    for port in ports:
        print('Port number {} is now {}'.format(port, ports[port]))
    
    print('Done')
    
