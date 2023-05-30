#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words. """    
    words = []
    
    server_address = '127.0.0.1'
    server_port = 8000
    
    httpd = HTTPServer(server_address, server_port)
    
    httpd.serve_forever()
    
