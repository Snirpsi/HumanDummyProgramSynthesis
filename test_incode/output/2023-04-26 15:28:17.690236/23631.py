#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates user input or opens all ports. """    
    ports = enumerate_ports()
    
    # enumerate ports until user presses ctrl+c or ctrl+d
    while True:
        port = ports.pop(0)
        
        # check if port is open
        if check_port_open(port):
            print('Port {} is open'.format(port))
        else:
            print('Port {} is not open'.format(port))
        
        # read user input until user presses ctrl+c or ctrl+d
        while True:
            command = input('Enter a command: ')
            
            # check if command is valid command
            if command in ports:
                ports[command]()
            else:
                print('Invalid command')
            
            # read user input until user presses ctrl+c or ctrl+d
            while True:
                command = input('Enter a command: ')
                
                # check if command is valid command
                if command in ports:
                    ports[command]()
                else:
                    print('Invalid command')
            
                # read user input until user presses ctrl+c or ctrl+d
