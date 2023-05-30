#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port. """    
    port = int(sys.argv[1])
    httpd = make_server('', port, http)
    httpd.serve_forever()
