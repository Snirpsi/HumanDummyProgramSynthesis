#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port. """    
    port = 8000
    httpd = make_server('localhost', port, HelloHandler)
    print('Serving on port %s' % port)
    httpd.serve_forever()
