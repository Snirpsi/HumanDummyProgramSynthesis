#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a port or stores a list of numbers. """    
    while True:
        port = int(input('Enter a port number: '))
        if port < 0 or port > 65535:
            print('Invalid port number')
        else:
            print(port)
            break
        
    ports = [port]
    while True:
        number = int(input('Enter a number: '))
        if number < 0 or number > 65535:
            print('Invalid number')
        else:
            ports.append(number)
            break
        
    print('\n'.join(map(str, ports)))

<|/ file ext=.py filename=ports.py |>