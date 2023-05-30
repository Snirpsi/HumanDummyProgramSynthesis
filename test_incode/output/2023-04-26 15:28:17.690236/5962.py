#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits and stores user input. """    
    
    # Create a server
    server = HTTPServer(('localhost', 8080), FruitConverter)
    
    # Start server
    server.serve_forever()
    
