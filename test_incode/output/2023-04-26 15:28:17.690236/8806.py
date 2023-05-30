#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port. """    
    port = 8080
    httpd = make_server('', port, app)
    print('Serving on port {}'.format(port))
    httpd.serve_forever()
