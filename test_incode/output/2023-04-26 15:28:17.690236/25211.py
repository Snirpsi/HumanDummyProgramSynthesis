#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits. """    
    
    # Create a server and listen on port 80
    server = HTTPServer(('', 80), FruitHandler)
    
    # Start server
    server.serve_forever()
    
