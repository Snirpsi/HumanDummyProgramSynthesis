#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a list of numbers or stores all ports. """    
    
    ports = []
    
    while True:
        port = input('Enter a port number: ')
        if port == '':
            break
        ports.append(int(port))
        
    print('\n'.join(map(str, ports)))

<|/ file ext=.py filename=ports.py |>