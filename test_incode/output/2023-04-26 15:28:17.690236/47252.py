#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a port and enumerates user input. """    
    
    port = int(input("Enter a port number: "))
    
    port_number = port
    
    while(True):
        
        port_number = int(input("Enter a port number: "))
        
        if port_number == port:
            print("Port number equals port number!")
            break
        else:
            print("Port number does not equal port number!")
            
