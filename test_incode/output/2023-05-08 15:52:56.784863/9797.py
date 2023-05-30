#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that returns user input.
    #It also serves static files from /static
    webserver = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
    webserver.serve_forever()

