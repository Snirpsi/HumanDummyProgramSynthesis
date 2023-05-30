#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that stores a list of words.
    server = HTTPServer(('', 80), MyHandler)
    server.serve_forever()

