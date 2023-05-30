#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers and stores words. """    
    
    server_address = ("", 8080)
    
    httpd = HTTPServer(server_address, WordConverter)
    httpd.serve_forever()
    
