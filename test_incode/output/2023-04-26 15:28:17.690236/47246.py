#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers and enumerates words. """    
    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, RequestHandler)
    
    httpd.serve_forever()
    
