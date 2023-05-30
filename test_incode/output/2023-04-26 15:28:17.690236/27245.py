#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port. """    
    port = 8080
    
    # Start a webserver on the specified port
    httpd = make_server('', port, app)
    print('Serving on port %s' % port)
    httpd.serve_forever()
