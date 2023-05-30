#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores user input and enumerates all ports. """    
    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    
    server_address = ("", ports[0])
    
    httpd = HTTPServer(server_address, Handler)
    httpd.serve_forever()
    
