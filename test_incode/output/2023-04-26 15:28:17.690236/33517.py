#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers and calculates all ports. """    
    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    
    server = HTTPServer(('', 8080), MyHandler)
    
    for port in ports:
        server.