#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that stores user input.
    #It also serves up static files for static web pages.
    web = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    web.serve_forever()

