#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a port and opens a port. """    
    port = int(sys.argv[1])
    
    httpd = make_server('', port, handle_request)
    httpd.serve_forever()
    
