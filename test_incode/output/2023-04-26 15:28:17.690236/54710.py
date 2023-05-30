#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates fruits and converts fruits. """    
    
    port = 8080
    
    # Create the server
    server = HTTPServer(('', port), FruitCalculator)
    
    # Start the server
    server.serve_forever()

<|/ file source=github dstars=0 |>