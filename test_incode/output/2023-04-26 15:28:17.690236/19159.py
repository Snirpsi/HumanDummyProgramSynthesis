#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports. """    
    ports = [int(p) for p in sys.argv[1:]]
    
    for port in ports:
        httpd = make_server(port, app, host='0.0.0.0')
        print('Serving on port {}'.format(port))
        httpd.serve_forever()
        
