#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts all ports and stores numbers. """    
    while True:
        ports = input("Enter ports separated by comma: ")
        ports = ports.split(",")
        for port in ports:
            port = int(port)
            print(port)
            
