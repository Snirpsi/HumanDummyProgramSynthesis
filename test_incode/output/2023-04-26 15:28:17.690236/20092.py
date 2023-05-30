#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over user input and adds all ports. """    
    ports = []
    while True:
        port = input('Enter a port number: ')
        if port == '':
            break
        ports.append(port)
    print('Ports found:', ports)
    
<|/ file source=github |>