#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port or multiplyes numbers. """    
    port = int(sys.argv[1])
    
    if port == 0:
        print('Usage: %s PORT' % sys.argv[0])
        sys.exit(0)
    
    httpd = make_server('', port, MyHandler)
    httpd.serve_forever()
    
