#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port. """    
    port = int(sys.argv[1])
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    print('serving at port %s' % port)
    httpd.serve_forever()
