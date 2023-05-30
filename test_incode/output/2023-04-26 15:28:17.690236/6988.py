#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <port>' % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    httpd = make_server(port, SimpleHTTPRequestHandler)
    print('Serving at port %s' % port)
    httpd.serve_forever()

<|/ file ext=.py filename=server.py |>