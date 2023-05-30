#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports. """    
    
    server_address = ("", 80)
    
    httpd = HTTPServer(server_address, RequestHandler)
    httpd.serve_forever()
    
