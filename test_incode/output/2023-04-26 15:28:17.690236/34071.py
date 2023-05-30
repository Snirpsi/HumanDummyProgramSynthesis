#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports or enumerates a list of words. """    
    
    port = 8080
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, Handler)
    httpd.serve_forever()
    
