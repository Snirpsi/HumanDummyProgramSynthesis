#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that stores words.
    httpd = HTTPServer(('localhost', 8080), WordsHandler)
    httpd.serve_forever()

