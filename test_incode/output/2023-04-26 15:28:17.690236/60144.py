#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a port or removes a list of numbers. """    
    
    ports = input("Enter a port number: ")
    
    ports = ports.split()
    
    if len(ports) == 2:
        
        ports.remove(ports[0])
        
        print(ports)
        
    else:
        print("Invalid input")
    
