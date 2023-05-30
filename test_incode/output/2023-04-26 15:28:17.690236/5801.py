#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input or opens all ports. """    
    
    ports = []
    
    # Open all ports
    for port in range(1024):
        ports.append(port)
        
    # Print user input
    while True:
        command = input('Enter a command: ')
        if command == 'exit':
            break
        else:
            ports[int(command)-1].send('OK')
            
    # Print all ports
    for port in ports:
        port.send('OK')
    
    # Close all ports
    for port in ports:
        port.close()
    
