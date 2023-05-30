#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates fruits. """    
    
    port = int(sys.argv[1])
    
    server = WSGIServer(('', port), FruitCalculator)
    server.serve_forever()

<|/ file source=github ext=.py |>