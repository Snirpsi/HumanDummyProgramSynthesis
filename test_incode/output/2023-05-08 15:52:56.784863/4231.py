#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that stores a list of words.
    httpd = HTTPServer(('localhost', 8000), WordsHandler)
    httpd.serve_forever()

