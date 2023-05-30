#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers. """    
    
    port = 8000
    
    httpd = HTTPServer(('', port), NumbersHandler)
    httpd.serve_forever()
