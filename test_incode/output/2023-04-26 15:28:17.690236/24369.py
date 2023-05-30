#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers. """    
    
    port = 8080
    
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
    print("Serving at port 