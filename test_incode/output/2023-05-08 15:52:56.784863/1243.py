#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that calculates a list of words.
    #It will listen on port 8000 and will print out the words in that list.
    #It will also print out the words in reverse order.
    server = HTTPServer(('', 8000), WordsHandler)
    server.serve_forever()

