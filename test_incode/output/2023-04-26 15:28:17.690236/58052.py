#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports. """    
    ports = [8080, 8081, 8082]
    
    server_address = ("", ports[0])
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    for port in ports[1:]:
        server_address = ("", port)
        httpd.