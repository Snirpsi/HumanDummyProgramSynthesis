#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers and adds all ports. """    
    ports = [8080, 8081, 8082]
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, Handler)
    
    httpd.serve_forever()
