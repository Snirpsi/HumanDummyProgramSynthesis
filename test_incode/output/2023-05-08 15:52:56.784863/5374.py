#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that iterates over user input.
    server = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    server.serve_forever()

