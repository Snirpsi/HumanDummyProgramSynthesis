#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers and multiplyes all ports. """    
    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    
    for port in ports:
        httpd = HTTPServer(('', port), MyHandler)
        httpd.serve_forever()
        
