#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of numbers or adds numbers. """    
    
    port = 8080
    
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
    print("Serving on port " + str(port))
    httpd.serve_forever()
