#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that removes words.
    server = HTTPServer(("", 80), WordRemover())
    server.serve_forever()

