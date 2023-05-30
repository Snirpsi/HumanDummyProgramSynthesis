#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input. """    
    
    # Define the port to listen on
    port = 8080
    
    # Define the handler to handle incoming requests
    handler = RequestHandler
    
    # Instantiate the server
    server = HTTPServer(('', port), handler)
    
    # Start the server
    server.serve_forever()
    
