#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits or stores user input. """    
    
    server = HTTPServer(("", 80), FruitServer)
    server.serve_forever()

<|/ file filename=server.py ext=.py |>