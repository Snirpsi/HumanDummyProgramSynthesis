#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port. """    
    port = int(sys.argv[1])
    httpd = make_server('', port, print_port)
    httpd.serve_forever()
    
