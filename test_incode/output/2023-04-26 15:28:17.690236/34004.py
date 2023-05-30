#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens user input or returns all ports. """    
    while True:
        ports = input("Enter ports separated by comma: ")
        if ports.strip() == '':
            break
        else:
            ports = ports.split(',')
            for port in ports:
                port = int(port)
                