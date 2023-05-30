#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds numbers or calculates words. """    
    
    httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    httpd.serve_forever()