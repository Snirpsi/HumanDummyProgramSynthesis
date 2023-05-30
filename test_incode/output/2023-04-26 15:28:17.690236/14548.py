#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports. """    
    ports = [int(port) for port in sys.argv[1:]]
    
    for port in ports:
        print('serving port {}'.format(port))
        
        httpd = make_server('', port, app)
        httpd.serve_forever()
        
