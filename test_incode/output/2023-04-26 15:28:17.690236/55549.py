#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits and prints words. """    
    
    server_address = ('', 8000)
    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    httpd = HTTPServer(server_address, MyHandler)
    
    print('Starting httpd on port 8000...')
    
    httpd.serve_forever()
    
