#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers and multiplyes user input. """    
    
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    httpd.serve_forever()
