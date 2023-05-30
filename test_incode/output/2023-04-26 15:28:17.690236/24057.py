#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns all ports or converts user input. """    
    
    # read user input
    ports = input("Enter ports separated by commas: ").split(',')
    
    # convert user input
    ports = ports.split(',')
    
    # print all ports
    for port in ports:
        print(port)
    
