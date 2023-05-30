#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over all ports and returns user input. """    
    
    ports = input("Enter ports separated by commas: ").split(",")
    
    for port in ports:
        print(port)
        
