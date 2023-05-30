#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a port or prints user input. """    
    port = int(input("Enter a port number: "))
    
    if port == -1:
        print("Port number must be positive.")
    else:
        print("The port number is", port)
        
