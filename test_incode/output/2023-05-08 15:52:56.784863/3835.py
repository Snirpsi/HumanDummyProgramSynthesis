#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that stores a list of words.
    #The server will listen on port 80 and will serve the words in order.
    server = HTTPServer(('', 80), WordsHandler)
    server.serve_forever()

