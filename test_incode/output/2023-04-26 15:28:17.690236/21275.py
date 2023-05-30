#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over fruits. """    
    
    # Create a server
    server = HTTPServer(('', 8000), FruitHandler)
    
    # Start the server
    server.serve_forever()
