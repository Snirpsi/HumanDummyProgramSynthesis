#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input. """    
    
    # Get the command line arguments.
    args = sys.argv[1:]
    
    # Get the port number from the command line arguments.
    port = int(args[0])
    
    # Get the user input from the command line arguments.
    user = args[1]
    
    # Start the webserver.
    webserver(port, user)
    
