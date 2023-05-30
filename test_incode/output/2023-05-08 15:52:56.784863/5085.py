#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that adds words.
    server = HTTPServer(("", 80), WordsHandler)
    server.serve_forever()

