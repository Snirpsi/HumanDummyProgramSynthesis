#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds all ports or multiplyes user input. """    
    
    ports = input("Enter the ports separated by comma: ").split(',')
    
    for port in ports:
        print(port*int(input("Enter the port number: ")))
    
    
