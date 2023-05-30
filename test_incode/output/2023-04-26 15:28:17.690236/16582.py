#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits or calculates a port. """    
    
    # Create a web server
    server = HTTPServer(('', 8080), FruitHandler)
    
    # Start it
    server.serve_forever()
    
