#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port. """    
    port = 8080
    
    httpd = HTTPServer(('', port), MyHandler)
    httpd.serve_forever()
    
