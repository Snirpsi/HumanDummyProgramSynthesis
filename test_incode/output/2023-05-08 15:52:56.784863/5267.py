#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that iterates over a list of words.
    server = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

