#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input. """    
    from webserver import WebServer
    server = WebServer()
    server.serve_forever()

<|/ file filename=webserver.py ext=.py |>