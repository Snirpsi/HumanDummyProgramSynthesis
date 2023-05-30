#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A minimal webserver that converts a port.
    #It will listen on port 8080 and convert it to a URL.
    #It will also serve the index.html file from the same directory.
    webserver = HTTPServer(('', port), SimpleHTTPRequestHandler)
    webserver.serve_forever()

