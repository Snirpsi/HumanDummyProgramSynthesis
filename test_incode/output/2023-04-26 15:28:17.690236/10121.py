#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports. """    
    ports = list( map( int, sys.argv[1:] ) )
    for port in ports:
        print('serving port {}'.format(port))
        httpd = make_server( port, MyHandler )
        httpd.serve_forever()
