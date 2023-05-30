#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input and stores all ports. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import argparse
    parser = argparse.ArgumentParser(description='Enumerate ports')
    parser.add_argument('port', nargs='?', type=int, help='port to enumerate')
    args = parser.parse_args()
    port = args.port
    httpd = HTTPServer(('', port), MyHandler)
    print('Serving at port %s' % port)
    httpd.serve_forever()

<|/ file ext=.py source=github |>