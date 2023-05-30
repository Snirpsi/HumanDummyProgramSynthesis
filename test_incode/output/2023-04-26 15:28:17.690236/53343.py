#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers. """    
    port = int(sys.argv[1])
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    sa = httpd.socket.getsockname()
    print("Serving HTTP on port %d" % sa[1])
    httpd.serve_forever()
