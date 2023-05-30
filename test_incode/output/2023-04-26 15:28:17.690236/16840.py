#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints all ports and iterates over user input. """    
    while True:
        ports = input("Enter a port number separated by space: ")
        ports = ports.split()
        for port in ports:
            print(port)
