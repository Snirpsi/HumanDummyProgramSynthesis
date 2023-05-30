#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports. """    
    ports = [int(p) for p in sys.argv[1:]]
    ports.sort()
    
    for port in ports:
        print('Serving on port {}'.format(port))
        
        httpd = make_server('', port, Handler)
        httpd.serve_forever()
        
