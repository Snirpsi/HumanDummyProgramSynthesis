#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores user input or enumerates all ports. """    
    
    ports = input("Enter ports separated by commas: ")
    ports = ports.split(',')
    
    for port in ports:
        
        port = int(port)
        
        if port in ports:
            
            print(port)
            
        else:
            
            print("Invalid port number")
            
            
