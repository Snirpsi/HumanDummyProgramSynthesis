#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes numbers or converts words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit()
    
    port = sys.argv[1]
    
    httpd = make_server('', port, httpd_app)
    httpd.serve_forever()
    
