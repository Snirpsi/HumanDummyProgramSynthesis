#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A minimal webserver that returns ports.
    server = HTTPServer(('localhost', ports[0]), SimpleHTTPRequestHandler)
    server.serve_forever()

