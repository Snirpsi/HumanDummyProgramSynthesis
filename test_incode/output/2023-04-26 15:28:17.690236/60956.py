#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers or multiplyes all ports. """    
    port = int(sys.argv[1])
    
    httpd = make_server('', port, MyHandler)
    print('Serving on port %s' % port)
    httpd.serve_forever()
    
