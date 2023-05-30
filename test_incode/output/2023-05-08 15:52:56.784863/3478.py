#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that removes a list of words.
    server = BaseHTTPServer.HTTPServer(('localhost', 8080), WordsHandler)
    server.serve_forever()

