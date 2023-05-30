#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes user input. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python -m webserver")
        sys.exit(1)
    
    httpd = make_server('', 8000, app)
    httpd.serve_forever()

<|/ file source=github ext=.py |>