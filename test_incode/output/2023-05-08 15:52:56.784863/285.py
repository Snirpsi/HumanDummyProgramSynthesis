#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that iterates over user input.
    import sys
    port = int(sys.argv[1])
    web = HTTPServer(("", port), SimpleHTTPRequestHandler)
    web.serve_forever()

