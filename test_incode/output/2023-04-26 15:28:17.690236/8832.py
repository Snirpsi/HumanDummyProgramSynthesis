#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes user input and enumerates all ports. """    
    
    ports = []
    
    while True:
        port = input("Enter a port number: ")
        if port == '':
            break
        ports.append(port)
    
    for port in ports:
        print(port)
        
