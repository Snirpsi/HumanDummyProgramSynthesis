#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns all ports and multiplyes user input. """    
    ports = []
    while True:
        try:
            ports.append(int(input('Enter a port number: ')))
        except ValueError:
            print('Invalid port number')
        else:
            break
    ports = list(map(lambda x: x * 2, ports))
    print('Ports used: ' + str(ports))
    
<|/ file ext=.py source=github |>