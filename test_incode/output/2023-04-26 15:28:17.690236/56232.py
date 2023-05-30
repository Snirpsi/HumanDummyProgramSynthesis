#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a list of numbers or prints all ports. """    
    
    ports = input("Enter the ports separated by comma: ").split(",")
    
    for port in ports:
        remove_port(port)
    
    print("All ports removed")
    
