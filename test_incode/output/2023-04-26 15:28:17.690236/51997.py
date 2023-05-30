#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns all ports or opens numbers. """    
    ports = []
    while True:
        try:
            ports.append(int(input('Enter a port number: ')))
        except ValueError:
            print('Invalid port number')
        else:
            break
    print('\n'.join(map(str, ports)))
    
