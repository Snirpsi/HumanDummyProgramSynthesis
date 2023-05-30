#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints all ports. """    
    ports = listen_ports()
    for port in ports:
        print(port)

<|/ file filename=