#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that iterates over words.
    server = HTTPServer(("", 80), MyHandler)
    server.serve_forever()

