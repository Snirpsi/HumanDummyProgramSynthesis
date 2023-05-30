#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that requests words.
    server = HTTPServer(('localhost', 8000), WordsHandler)
    server.serve_forever()

