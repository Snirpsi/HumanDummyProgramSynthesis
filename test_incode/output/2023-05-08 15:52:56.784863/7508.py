#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that returns words.
    server = HTTPServer(('', 8000), WordsHandler)
    print('Starting server')
    server.serve_forever()

