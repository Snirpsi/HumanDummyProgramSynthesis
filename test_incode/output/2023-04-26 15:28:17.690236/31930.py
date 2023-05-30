#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port and prints all ports. """    
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    httpd.serve_forever()
