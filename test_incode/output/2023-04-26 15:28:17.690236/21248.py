#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('usage: fruits.py [port]')
        sys.exit(1)
    
    port = sys.argv[1]
    
    httpd = make_server(port, FruitHandler)
    httpd.serve_forever()

<|/ file source=github ext=.py |>