#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of numbers and opens a port. """    
    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    httpd = make_server('', port, Server)
    httpd.serve_forever()
    
