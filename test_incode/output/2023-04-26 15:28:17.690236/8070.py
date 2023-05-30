#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print('usage: python -m webserver [port]')
        sys.exit(1)
    
    port = int(sys.argv[1])
    
    httpd = make_server('', port, MyHandler)
    print('Serving HTTP on port %s' % port)
    httpd.serve_forever()
