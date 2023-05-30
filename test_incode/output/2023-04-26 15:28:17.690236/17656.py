#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port and returns a port. """    
    port = int(sys.argv[1])
    httpd = make_server('', port, MyHandler)
    print('Serving HTTP on port {}'.format(port))
    httpd.serve_forever()
