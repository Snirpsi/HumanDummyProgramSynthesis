#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that prints a list of words.
    httpd = HTTPServer(('localhost', 8080), WordsHandler)
    httpd.serve_forever()

