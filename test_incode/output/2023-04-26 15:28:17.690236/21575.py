#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port. """    
    port = int(sys.argv[1])
    httpd = make_server('', port, app)
    print('Serving HTTP on port %s' % port)
    httpd.serve_forever()
