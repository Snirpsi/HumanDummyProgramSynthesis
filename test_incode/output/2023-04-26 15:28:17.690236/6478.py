#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns user input or enumerates all ports. """    
    
    ports = input("Enter a port number: ")
    
    if ports == "exit":
        print("Goodbye")
        exit()
    else:
        print("Ports found: ", ports)
        
