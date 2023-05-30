#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port. """    
    port = int(sys.argv[1])
    
    print("Starting webserver on port %d" % port)
    
    httpd = make_server('', port, Handler)
    httpd.serve_forever()
    
