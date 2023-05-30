#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port. """    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), MyHandler)
    print('Serving on port %s' % port)
    httpd.serve_forever()
