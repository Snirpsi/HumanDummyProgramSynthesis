#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port or adds a list of words. """    
    port = int(sys.argv[1])
    
    if port == 0:
        port = 8080
    
    httpd = make_server('', port, MyHandler)
    httpd.serve_forever()

<|/ file source=github ext=.py |>