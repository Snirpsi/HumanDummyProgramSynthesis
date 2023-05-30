#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port. """    
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, Handler)
    
    print('Starting server on port 8080')
    httpd.serve_forever()
    
