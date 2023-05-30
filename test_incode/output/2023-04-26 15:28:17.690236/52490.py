#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports and returns a port. """    
    port = 0
    while port < 65536:
        port += 1
        print('Serving on port %s' % port)
        httpd = make_server('localhost', port, app)
        httpd.serve_forever()
