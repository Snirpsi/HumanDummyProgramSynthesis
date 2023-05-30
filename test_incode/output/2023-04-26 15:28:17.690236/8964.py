#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port or prints user input. """    
    
    port = int(sys.argv[1])
    
    if port == 8080:
        print("Welcome to port 8080")
    else:
        print("Please enter a port number between 1 and 8080")
        
