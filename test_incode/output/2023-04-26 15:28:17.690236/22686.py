#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers or opens numbers. """    
    
    port = 8080
    
    server_address = ("", port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print("Serving at port", port)
    httpd.serve_forever()
    
