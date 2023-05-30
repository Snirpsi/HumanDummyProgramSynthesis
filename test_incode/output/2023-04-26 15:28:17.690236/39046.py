#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates words and enumerates a port. """    
    
    # Start the server
    server = WSGIServer(('', 8080), app)
    
    # Run the server
    server.serve_forever()
    
