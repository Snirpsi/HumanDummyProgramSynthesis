#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that returns user input.
    import sys
    port = 8080
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    httpd.serve_forever()

