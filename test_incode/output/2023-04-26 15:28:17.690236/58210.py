#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers and enumerates a port. """    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    httpd = make_server(*server_address, RequestHandler)
    print('Serving HTTP on', server_address[0], 'port', port)
    httpd.serve_forever()
    
