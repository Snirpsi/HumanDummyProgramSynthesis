#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that requests a list of words.
    httpd = HTTPServer(("", 80), WordsHandler)
    httpd.serve_forever()

