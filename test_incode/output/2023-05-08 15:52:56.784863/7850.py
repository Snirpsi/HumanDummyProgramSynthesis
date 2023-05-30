#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that adds user input.
    webserver = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    webserver.serve_forever()

