#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports. """    
    ports = [8080, 8081, 8082]
    ports = [int(p) for p in ports]
    
    server_address = ("", ports[0])
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    httpd.serve_forever()
