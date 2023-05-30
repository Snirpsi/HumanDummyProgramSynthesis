#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that opens a list of words.
    webserver = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    webserver.serve_forever()

