#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that converts a list of words.
    server = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

