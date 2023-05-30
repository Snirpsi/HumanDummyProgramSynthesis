#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that opens user input.
    server = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    server.serve_forever()

