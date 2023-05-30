#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores numbers or prints a list of numbers. """    
    
    server_address = '0.0.0.0'
    server_port = 5000
    
    httpd = HTTPServer(server_address, server_port)
    httpd.serve_forever()
    
