#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores user input. """    
    
    server = HTTPServer(("", 8000), Handler)
    server.serve_forever()

<|/ file ext=.py source=github |>