#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds user input or returns all ports. """    
    ports = []
    while True:
        ports.append(input('Port: '))
        if len(ports) == 2:
            break
        else:
            print('Invalid input')
    
    print('\n'.join(ports))
    
