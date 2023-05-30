#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that returns user input.
    webserver = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    webserver.serve_forever()

