#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits. """    
    
    # Create the server
    server = HTTPServer(('', 80), FruitHandler)
    
    # Start the server
    server.serve_forever()
