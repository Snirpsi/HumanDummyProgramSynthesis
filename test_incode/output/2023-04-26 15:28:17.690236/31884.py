#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports. """    
    port = int(sys.argv[1])
    
    httpd = make_server('', port, Handler)
    httpd.serve_forever()
    
