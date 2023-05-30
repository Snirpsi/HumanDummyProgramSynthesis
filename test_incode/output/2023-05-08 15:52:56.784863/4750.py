#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that stores words.txt in the current directory
    import os
    webserver = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    webserver.serve_forever()

