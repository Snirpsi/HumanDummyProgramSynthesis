#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words or calculates all ports. """    
    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    
    server_address = ('', 8080)
    
    httpd = HTTPServer(server_address, WordsHandler)
    
    httpd.serve_forever()
    
