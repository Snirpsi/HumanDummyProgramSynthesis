#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of numbers or multiplyes a port. """    
    port = int(sys.argv[1])
    
    if port == 0:
        port = 8080
    
    web = WebServer()
    web.serve_forever()

<|/ file filename=server.py ext=.py |>