#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that opens user input.
    webserver = HTTPServer(('', 80), SimpleHTTPRequestHandler)
    webserver.serve_forever()

