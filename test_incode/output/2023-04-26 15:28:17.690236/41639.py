#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers or opens a list of words. """    
    
    words = ['cat', 'dog', 'mouse']
    
    port = 5000
    
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
    
    print("Serving on port {}".format(port))
    httpd.serve_forever()
    
