#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input. """    
    
    import sys
    
    webserver = Webserver()
    webserver.serve_forever()

<|/ file source=github filename=server.py |>