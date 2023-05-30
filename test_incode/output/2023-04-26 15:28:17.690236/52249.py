#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over fruits or adds a list of numbers. """    
    
    # Create a server instance
    server = HTTPServer(('', 8080), FruitHandler)
    
    # Start the server
    server.serve_forever()
    
