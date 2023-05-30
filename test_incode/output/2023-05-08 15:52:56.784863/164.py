#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that removes words.
    import sys
    import os
    webserver = HTTPServer(('', 8000), WordsHandler)
    webserver.serve_forever()

