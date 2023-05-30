#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A minimal webserver that stores a port.
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    print('serving at port', port)
    server.serve_forever()

