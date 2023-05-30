#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates fruits and opens a list of words. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), FruitServer)
    server.serve_forever()

<|/ file filename=server.py ext=.py |>