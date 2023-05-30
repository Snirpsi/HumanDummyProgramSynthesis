#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of numbers. """    
    
    port = 80
    
    httpd = HTTPServer(('', port), MyHandler)
    httpd.serve_forever()
    
