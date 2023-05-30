#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens all ports and prints user input. """    
    
    ports = []
    
    # Open all ports
    for port in range(1,65535):
        ports.append(port)
        
    # Print user input
    while True:
        port = input("Enter port number: ")
        if port in ports:
            print("Port number:", port)
        else:
            print("Port number not found")
            
