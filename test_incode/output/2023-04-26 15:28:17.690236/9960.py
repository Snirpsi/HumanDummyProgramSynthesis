#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port and stores fruits. """    
    while True:
        port = input('Enter a port number: ')
        fruits = convert_port(port)
        print('The fruits in port {} are: {}'.format(port, fruits))
        time.sleep(1)
