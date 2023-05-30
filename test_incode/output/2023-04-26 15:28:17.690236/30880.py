#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits or calculates a list of numbers. """    
    
    # Create a server
    server = HTTPServer(('', 8080), FruitCalculator)
    
    # Start the server
    server.serve_forever()
