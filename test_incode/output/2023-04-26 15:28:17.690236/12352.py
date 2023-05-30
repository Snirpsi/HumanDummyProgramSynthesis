#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    
    print('Serving at http://%s:8000/' % server_address)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    
    httpd.server_close()
    
    print('Server Stopped')

<|/ file filename=