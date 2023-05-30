#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds numbers and prints numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8080
    
    httpd = make_server('', port, MyHandler)
    httpd.serve_forever()

<|/ file filename=server.py ext=.py |>