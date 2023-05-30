#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers or removes a port. """    
    
    server_address = ("", 80)
    
    httpd = HTTPServer(server_address, RequestHandler)
    
    httpd.serve_forever()
