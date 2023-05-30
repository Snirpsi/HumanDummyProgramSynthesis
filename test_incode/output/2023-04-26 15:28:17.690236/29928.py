#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = make_server('', port, HelloHandler)
    
    print('Serving HTTP on port {port} ...'.format(port=port))
    
    httpd.serve_forever()
    
