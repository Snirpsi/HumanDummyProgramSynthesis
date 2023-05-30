#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits or prints user input. """    
    
    # Create a web server
    server = HTTPServer(('', 80), FruitHandler)
    
    # Start it
    server.serve_forever()

<|/ file source=github |>