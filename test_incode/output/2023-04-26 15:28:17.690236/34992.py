#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port and multiplyes numbers. """    
    
    port = 8080
    
    httpd = HTTPServer(('', port), MyHandler)
    httpd.serve_forever()
    
