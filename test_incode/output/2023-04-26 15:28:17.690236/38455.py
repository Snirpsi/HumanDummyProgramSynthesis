#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers and returns user input. """    
    
    httpd = HTTPServer(('', 8000), MyHandler)
    httpd.serve_forever()
    
