#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes user input and calculates numbers. """    
    
    server_address = '0.0.0.0'
    port = 8080
    
    httpd = HTTPServer(server_address, port)
    httpd.serve_forever()
