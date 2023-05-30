#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers and opens a list of numbers. """    
    
    port = 8080
    
    httpd = make_server('', port, app)
    print('Serving on port %s' % port)
    httpd.serve_forever()

<|/ file ext=.py source=github |>