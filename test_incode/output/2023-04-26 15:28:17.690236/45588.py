#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers or prints user input. """    
    
    port = 8080
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    httpd.serve_forever()
    
