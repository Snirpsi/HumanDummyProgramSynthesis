#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits or calculates user input. """    
    
    server = HTTPServer(('', 8080), FruitCalculator)
    server.serve_forever()
    
