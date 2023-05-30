#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports. """    
    ports = [int(i) for i in sys.argv[1:]]
    
    for port in ports:
        print('Serving on port {}'.format(port))
        httpd = make_server('', port, app)
        httpd.serve_forever()
