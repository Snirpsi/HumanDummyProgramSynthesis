#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that returns a list of words.
    server = HTTPServer(('localhost', 8080), WordsHandler)
    server.serve_forever()

