#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port. """    
    
    port = sys.argv[1]
    
    httpd = make_server('', port, MyHandler)
    print('Serving on port {}'.format(port))
    httpd.serve_forever()
    
