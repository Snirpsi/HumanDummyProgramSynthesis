#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input or adds user input. """    
    
    # Define the webserver address
    address = '0.0.0.0'
    
    # Define the port number
    port = 8080
    
    # Define the webserver handler
    handler = SimpleHTTPRequestHandler
    
    # Define the webserver 