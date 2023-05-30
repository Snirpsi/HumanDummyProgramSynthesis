#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words or prints all ports. """    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    
    httpd = HTTPServer(("", ports[0]), Handler)
    httpd.serve_forever()
