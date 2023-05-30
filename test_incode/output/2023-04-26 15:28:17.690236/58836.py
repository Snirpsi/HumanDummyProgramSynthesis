#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port and prints a port. """    
    port = int(sys.argv[1])
    print('Serving on port {}'.format(port))
    httpd = make_server('', port, HelloHandler)
    httpd.serve_forever()