#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports and converts user input. """    
    
    ports = []
    
    # Open ports
    for port in range(1, 65535):
        ports.append(port)
    
    # Convert user input
    while True:
        command = input('Enter a command: ')
        
        # Convert command
        if command == 'exit':
            break
        elif command == 'add':
            ports.append(int(input('Enter a port: ')))
        elif command == 'remove':
            ports.remove(int(input('Enter a port: ')))
        elif command == 'list':
            print('\n'.join(map(str, ports)))
        elif command == 'clear':
            ports = []
        else:
            print('Unknown command')
            
    # Close ports
    for port in ports:
        