#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A minimal webserver that removes a port.
    webserver = HTTPServer(('', port), SimpleHTTPRequestHandler)
    webserver.serve_forever()

