#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A endless loop that converts a port.
    while True:
        port = port + 1
        
        #A simple HTTP server that converts a port.
        httpd = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
        httpd.serve_forever()

