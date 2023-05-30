#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input and returns a port. """    
    port = int(input("Enter a port number: "))
    
    webserver.run(port)
    
