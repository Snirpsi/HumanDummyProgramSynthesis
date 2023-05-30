#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that enumerates words.
    server = HTTPServer(('', 8080), WordEnumerator)
    server.serve_forever()

