#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports and opens all ports. """    
    
    ports = [8080, 8081, 8082]
    
    for port in ports:
        httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
        httpd.serve_forever()
    
