#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that adds user input.
    #It will also serve the static files from /static
    webserver = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    webserver.serve_forever()

