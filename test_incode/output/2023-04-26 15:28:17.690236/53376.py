#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a port and returns user input. """    
    ports = [port for port in range(1,65535)]
    
    while True:
        port = input("Enter a port number: ")
        if port in ports:
            print(port)
        else:
            print("That port doesn't exist!")
            
