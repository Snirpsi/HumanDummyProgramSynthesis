#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port or multiplyes all ports. """    
    port = 1
    
    while True:
        port = port * 2
        print('Starting port %s' % port)
        httpd = make_server('', port, MyHandler)
        httpd.serve_forever()
    
