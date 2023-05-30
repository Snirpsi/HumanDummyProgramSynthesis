#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port or adds fruits. """    
    
    port = int(sys.argv[1])
    
    if port == 0:
        port = 5000
    
    httpd = make_server('', port, FruitHandler)
    
    print('Serving on port {}'.format(port))
    httpd.serve_forever()
    
