#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of numbers or converts all ports. """    
    ports = [8080, 8081, 8082]
    
    httpd = HTTPServer(("", ports[0]), SimpleHTTPRequestHandler)
    httpd.serve_forever()
    
