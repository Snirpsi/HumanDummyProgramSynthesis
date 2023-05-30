#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A endless loop that stores a port.
    while True:
        port = port + 1
        print("Port " + str(port))
        
        #A simple HTTP server that prints out the port number.
        httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
        httpd.serve_forever()

