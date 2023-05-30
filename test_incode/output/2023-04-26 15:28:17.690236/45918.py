#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds user input or multiplyes fruits. """    
    
    # Create a server
    server = HTTPServer(('', 8080), FruitServer)
    
    # Start it
    server.serve_forever()

<|/ file source=github filename=fruitserver.py |>