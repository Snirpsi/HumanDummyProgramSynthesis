#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words and calculates a list of numbers. """    
    
    import sys
    
    port = sys.argv[1]
    
    webserver = WebServer(port)
    webserver.serve_forever()

<|/ file filename=webserver.py source=github |>