#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes user input. """    
    
    webserver = WebServer()
    webserver.serve_forever()

<|/ file ext=.py source=github filename=webserver.py |>