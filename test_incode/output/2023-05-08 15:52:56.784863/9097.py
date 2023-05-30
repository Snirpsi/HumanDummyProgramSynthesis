#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that converts words.txt into html
    webserver = HTTPServer(("", 80), WordsHandler)
    webserver.serve_forever()

