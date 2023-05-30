#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts all ports or returns user input. """    
    
    # Convert ports
    ports = convert_ports()
    
    # Return user input
    choice = input('Do you want to convert all ports or just one? (y/n): ')
    
    # Convert ports
    if choice == 'y':
        ports = convert_ports()
    
    # Return user input
    if choice == 'n':
        print('Exiting...')
        exit()
    
    # Convert ports
    else:
        print('Exiting...')
        exit()
    
    # Print ports
    print('Ports:')
    for port in ports:
        print(port)
    
    # Print ports
    print('Done!')
    
