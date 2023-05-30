#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that iterates over words.
    server = HTTPServer(('localhost', 8000), Handler)
    server.serve_forever()

