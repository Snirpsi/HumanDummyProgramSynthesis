#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that returns words.
    httpd = HTTPServer(("", 80), WordsHandler)
    httpd.serve_forever()

