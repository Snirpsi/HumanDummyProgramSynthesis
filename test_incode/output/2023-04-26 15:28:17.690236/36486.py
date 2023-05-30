#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of numbers or removes a port. """    
    
    ports = input("Enter a port: ")
    
    if ports == "all":
        ports = range(1024)
    
    for port in ports:
        print(port)
        
