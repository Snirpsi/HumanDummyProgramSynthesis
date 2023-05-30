#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers and enumerates words. """    
    
    # Start webserver
    server = HTTPServer(("", 80), MyHandler)
    server.serve_forever()

<|/ file source=github filename=webserver.py |>