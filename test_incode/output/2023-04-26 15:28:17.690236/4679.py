#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input. """    
    
    import sys
    
    server_address = ('', 8080)
    
    httpd = HTTPServer(server_address, RequestHandler)
    httpd.serve_forever()
    
