#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers. """    
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, NumbersHandler)
    httpd.serve_forever()
    
