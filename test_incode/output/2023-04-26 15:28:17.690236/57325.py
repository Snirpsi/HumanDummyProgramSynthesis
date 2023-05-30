#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates user input. """    
    
    httpd = HTTPServer(("", 80), MyHandler)
    httpd.serve_forever()
