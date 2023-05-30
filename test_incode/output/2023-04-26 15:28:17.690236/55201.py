#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port or multiplyes a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s [port]" % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    httpd = make_server('', port, MyHandler)
    httpd.serve_forever()
    
