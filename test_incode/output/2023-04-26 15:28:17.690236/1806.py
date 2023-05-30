#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates fruits. """    
    
    HOST = '127.0.0.1'
    PORT = 8080
    
    httpd = HTTPServer(HOST, PORT)
    
    httpd.serve_forever()
    
