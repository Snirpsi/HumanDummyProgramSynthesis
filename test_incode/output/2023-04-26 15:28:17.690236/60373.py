#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port and converts all ports. """    
    while True:
        port = int(input('Enter a port number: '))
        
        try:
            port = int(port)
        except ValueError:
            print('Invalid port number')
            continue
        
        port = str(port)
        
        print('Port: ', port)
        
        ports.append(port)
        
        ports_converted.append(port)
        
        ports_converted.append('\n')
        
        print('Ports converted: ', ports_converted)
        
        print('\n')
        
