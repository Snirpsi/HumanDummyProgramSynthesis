#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes user input. """    
    port = int(sys.argv[1])
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    sa = httpd.socket.getsockname()
    print('Serving HTTP on port %s' % sa[1])
    httpd.serve_forever()
