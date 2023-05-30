#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port. """    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    httpd = make_server('', port, MyHandler)
    httpd.serve_forever()
    
