#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports or opens words. """    
    from wsgiref.simple_server import make_server
    import sys
    
    port = int(sys.argv[1])
    
    httpd = make_server('', port, MyApp)
    httpd.serve_forever()
    
