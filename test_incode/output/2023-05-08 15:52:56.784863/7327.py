#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that calculates words.
    httpd = HTTPServer(('', 80), WordsHandler)
    httpd.serve_forever()

