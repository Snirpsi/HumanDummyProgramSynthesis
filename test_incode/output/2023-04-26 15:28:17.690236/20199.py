#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port and converts user input. """    
    port = int(sys.argv[1])
    
    web = WebServer()
    web.serve_forever()
    
<|/ file ext=.py |>