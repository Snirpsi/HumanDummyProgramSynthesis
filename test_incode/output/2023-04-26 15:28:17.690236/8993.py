#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits or stores a list of numbers. """    
    
    # Create the server
    server = HTTPServer(('', 80), FruitServer)
    
    # Run the server
    server.serve_forever()

<|/ file source=github filename=server.py |>