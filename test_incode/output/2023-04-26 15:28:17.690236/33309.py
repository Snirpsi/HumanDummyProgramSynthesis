#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port and opens numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('localhost', port), MyHandler)
    print('Serving on port %s' % port)
    httpd.serve_forever()
    
