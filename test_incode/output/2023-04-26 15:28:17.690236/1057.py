#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens user input and stores all ports. """    
    
    ports = []
    while True:
        port = input("Enter a port number: ")
        if port in ports:
            print("Port number already in use.")
        else:
            ports.append(port)
    
    print("\nPorts used:")
    for port in ports:
        print(port)
        
    
<|/ file ext=.py filename=ports.py |>