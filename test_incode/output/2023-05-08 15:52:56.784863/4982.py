#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that opens a list of words.
    webserver = HTTPServer(('', 8000), WordsHandler)
    webserver.serve_forever()

