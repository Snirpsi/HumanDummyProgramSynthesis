#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores user input. """    
    
    import sys
    
    httpd = HTTPServer(('', 8000), MyHandler)
    httpd.serve_forever()
    
