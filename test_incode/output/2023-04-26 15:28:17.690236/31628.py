#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers. """    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()
    
