#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that opens a list of words.
    httpd = HTTPServer(('', 8000), WordsHandler)
    httpd.serve_forever()

