#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits or converts user input. """    
    
    # Create a webserver object
    server = HTTPServer(('', 8080), FruitHandler)
    
    # Run the server
    server.serve_forever()
