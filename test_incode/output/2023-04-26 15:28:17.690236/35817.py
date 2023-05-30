#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers or opens numbers. """    
    port = int(sys.argv[1])
    
    httpd = make_server('', port, app)
    print('Serving at port %d...' % port)
    httpd.serve_forever()

<|/ file ext=.py filename=server.py |>