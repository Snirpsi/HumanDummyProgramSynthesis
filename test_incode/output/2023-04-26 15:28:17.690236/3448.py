#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = make_server('localhost', port, Handler)
    print('Serving on port %s' % port)
    httpd.serve_forever()
    
