#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that enumerates words.
    httpd = HTTPServer(('', 8080), WordsHandler)
    httpd.serve_forever()

