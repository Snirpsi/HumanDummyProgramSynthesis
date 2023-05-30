#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds numbers. """    
    import sys
    from wsgiref.simple_server import make_server
    
    port = sys.argv[1]
    
    httpd = make_server('localhost', port, NumberHandler)
    print('Serving on port %s' % port)
    httpd.serve_forever()
    
