#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port or adds user input. """    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('port', type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port
    httpd = HTTPServer(("", port), MyHandler)
    print("Serving on port {}".format(port))
    httpd.serve_forever()
