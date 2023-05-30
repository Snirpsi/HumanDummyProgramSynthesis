#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port or stores all ports. """    
    port = int(sys.argv[1])
    
    if port == 0:
        port = 1
    
    httpd = make_server("", port, MyHandler)
    httpd.serve_forever()
    
