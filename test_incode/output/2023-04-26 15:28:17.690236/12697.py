#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes user input. """    
    
    import sys
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    
    print('Serving HTTP on port 8080...')
    httpd.serve_forever()
    
