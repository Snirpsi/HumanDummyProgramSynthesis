#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers or adds all ports. """    
    ports = []
    while True:
        ports.append(int(input('Enter a port number: ')))
        if len(ports) == 3:
            break
    print('The ports are:')
    for port in ports:
        print(port)
    print('The sum of the ports is:', sum(ports))
