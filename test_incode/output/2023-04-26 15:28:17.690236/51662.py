#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports and prints a list of numbers. """    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    httpd = make_server(*server_address, Handler)
    httpd.serve_forever()
