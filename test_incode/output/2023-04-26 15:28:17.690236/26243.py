#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates user input or multiplyes a list of words. """    
    
    server_address = 'localhost'
    server_port = 8080
    
    httpd = HTTPServer(server_address, server_port)
    httpd.serve_forever()
