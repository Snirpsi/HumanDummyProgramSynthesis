#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a port. """    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, RequestHandler)
    httpd.serve_forever()
    
