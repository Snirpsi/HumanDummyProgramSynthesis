#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits or converts words. """    
    
    server_address = '0.0.0.0'
    server_port = 8080
    
    httpd = HTTPServer(server_address, server_port)
    
    httpd.serve_forever()
    
