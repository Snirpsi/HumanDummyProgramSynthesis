#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words. """    
    
    words = ["cat", "dog", "bird", "snake", "mouse", "fox"]
    
    server_address = ("", 8000)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    httpd.serve_forever()
    
