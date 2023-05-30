#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports. """    
    ports = []
    for port in range(1, 65535):
        ports.append(port)
    
    httpd = HTTPServer(('', 0), SimpleHTTPRequestHandler)
    httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='server.key', certfile='server.crt')
    httpd.serve_forever()
    
    print('Serving on port', httpd.server_address[1])
    
