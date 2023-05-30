#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes numbers or iterates over user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 5000
    
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
    
    print("Serving at port", port)
    httpd.serve_forever()
