#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that stores a list of words.
    server = HTTPServer(('', 8000), WordsHandler)
    server.serve_forever()

