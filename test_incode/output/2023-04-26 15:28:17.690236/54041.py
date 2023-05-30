#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints user input or removes a port. """    
    port = int(input("Enter a port number: "))
    
    if port == -1:
        print("Invalid port number")
    else:
        print("Port number " + str(port))
        
