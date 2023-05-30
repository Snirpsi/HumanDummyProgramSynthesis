#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints user input or returns all ports. """    
    
    ports = []
    
    while True:
        ports.append(input('Enter port number or q to quit: '))
        
        if ports[-1] == 'q':
            break
    
    print('\n'.join(ports))
    
