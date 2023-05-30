#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that adds a list of words.
    #It will respond with a simple HTML page with all the words in it.
    httpd = HTTPServer(('', 80), SimpleHTTPRequestHandler)
    httpd.serve_forever()

