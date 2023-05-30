#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input or multiplyes a port. """    
    
    port = int(input("Enter a port number: "))
    
    if port > 0 and port <= 65535:
        print("The port number you entered is " + str(port))
    else:
        print("The port number you entered is " + str(port*2))
    
