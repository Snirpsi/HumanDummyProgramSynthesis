#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input or returns all ports. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('port', type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port
    httpd = HTTPServer(('', port), BaseHTTPRequestHandler)
    httpd.serve_forever()

<|/ file ext=.py source=github |>