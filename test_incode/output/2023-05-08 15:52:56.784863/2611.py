#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that calculates words.
    #It serves up index.html and calculates words in index.html.
    server = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

