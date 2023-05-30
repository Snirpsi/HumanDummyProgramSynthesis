#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports. """    
    
    port = 8080
    
    # Create a server to listen on port 8080
    server = HTTPServer(("", port), Handler)
    
    # Run the server
    server.serve_forever()
    
