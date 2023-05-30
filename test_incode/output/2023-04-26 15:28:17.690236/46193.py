#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a port or removes a list of words. """    
    
    ports = input("Enter a list of ports separated by commas: ")
    
    ports = ports.split(",")
    
    ports = [int(i) for i in ports]
    
    ports = list(set(ports))
    
    ports.sort()
    
    ports = ports[0: