#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that opens user input.
    web = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    web.serve_forever()

