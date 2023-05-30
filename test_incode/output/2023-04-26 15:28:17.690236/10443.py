#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports. """    
    ports = [8080, 8081, 8082]
    
    ports_server = HTTPServer(ports, SimpleHTTPRequestHandler)
    ports_server.serve_forever()
    
