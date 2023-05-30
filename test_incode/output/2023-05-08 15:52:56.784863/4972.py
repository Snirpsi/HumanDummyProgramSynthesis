#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that prints user input.
    server = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

