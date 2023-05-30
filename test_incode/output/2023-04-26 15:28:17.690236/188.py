#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates fruits. """    
    
    # Define the server
    server = HTTPServer(('', 8080), FruitCalculator)
    
    # Start the server
    server.serve_forever()

<|/ file ext=.py source=github |>