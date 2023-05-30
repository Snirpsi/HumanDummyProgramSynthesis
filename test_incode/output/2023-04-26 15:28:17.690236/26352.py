#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits and opens a list of words. """    
    
    # Create a server and a handler to handle requests from the client
    server = HTTPServer(("", 80), FruitHandler)
    
    # Start the server
    server.serve_forever()
