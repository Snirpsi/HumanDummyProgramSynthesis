#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers. """    
    
    server_address = 'localhost'
    server_port = 5000
    
    httpd = HTTPServer(server_address, server_port)
    
    httpd.serve_forever()
    
