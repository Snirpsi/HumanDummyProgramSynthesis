#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes numbers. """    
    port = 8080
    httpd = make_server('', port, MyHandler)
    print('Serving at port', port)
    httpd.serve_forever()

<|/ file ext=.py |>