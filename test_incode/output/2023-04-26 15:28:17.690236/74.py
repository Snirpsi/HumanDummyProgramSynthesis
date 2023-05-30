#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words and prints all ports. """    
    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    
    server_address = ("", ports[0])
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print("Serving HTTP on port {0}".format(ports[0]))
    
    httpd.serve_forever()
    
