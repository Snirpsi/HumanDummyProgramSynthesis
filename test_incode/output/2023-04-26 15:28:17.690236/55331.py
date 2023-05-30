#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports. """    
    ports = range(8000, 8100)
    
    httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
    
    for port in ports:
        httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='./server.key', certfile='./server.crt')
        httpd.serve_forever()
        
