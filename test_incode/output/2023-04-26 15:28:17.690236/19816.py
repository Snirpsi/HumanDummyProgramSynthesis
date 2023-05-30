#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits or multiplyes fruits. """    
    
    # Create a server
    server = HTTPServer(('', 8080), FruitMultiply)
    
    # Start it
    server.serve_forever()
    
