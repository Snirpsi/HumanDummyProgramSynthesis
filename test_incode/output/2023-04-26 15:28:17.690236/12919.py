#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over fruits and converts fruits. """    
    
    # Create a server and bind it to port 80
    server = HTTPServer(('', 80), FruitHandler)
    
    # Start server
    server.serve_forever()
    
