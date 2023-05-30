#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that removes a list of words.
    httpd = HTTPServer(('', 80), SimpleHTTPRequestHandler)
    httpd.serve_forever()

