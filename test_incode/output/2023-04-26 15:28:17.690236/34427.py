#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports. """    
    
    HOST = '0.0.0.0'
    PORT = 8080
    
    httpd = HTTPServer(HOST, PORT)
    
    httpd.serve_forever()
    
