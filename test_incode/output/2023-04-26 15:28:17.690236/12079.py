#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports or prints a port. """    
    port = int(sys.argv[1])
    
    httpd = make_server('', port, MyHandler)
    print('Serving on port %s' % port)
    httpd.serve_forever()
