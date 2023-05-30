#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that removes user input.
    server = HTTPServer(("", 80), SimpleHTTPRequestHandler)
    server.serve_forever()

