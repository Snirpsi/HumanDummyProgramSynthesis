#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A endless loop that iterates over a port.
    while True:
        time.sleep(1)
        
        #A simple HTTP server that prints out the current time.
        httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
        httpd.serve_forever()

