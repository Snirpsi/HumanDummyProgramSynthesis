#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of numbers and adds words. """    
    
    port = 8080
    
    server = HTTPServer(("", port), SimpleHTTPRequestHandler)
    print("Serving at port", port)
    
    server.serve_forever()
    
