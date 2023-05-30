#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports or multiplyes user input. """    
    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    
    ports = [int(port) for port in ports]
    
    server_address = ("", ports[0])
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    httpd.serve_forever()
