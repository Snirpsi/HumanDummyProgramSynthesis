#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input and removes user input. """    
    
    # Open the port on which the webserver will listen for connections.
    server_address = ('localhost', 8000)
    
    # Create the webserver and bind it to the address given.
    httpd = HTTPServer(server_address, RequestHandler)
    
    # Start the webserver.
    httpd.serve_forever()
    
