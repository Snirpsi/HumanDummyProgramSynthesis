#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that prints words.
    server = BaseHTTPServer.HTTPServer(('localhost', 8000), WordsHandler)
    server.serve_forever()

