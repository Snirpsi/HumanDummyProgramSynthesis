#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that requests words.
    #It will respond with an HTML page with all the words in words.
    httpd = HTTPServer(('', 8000), WordsHandler)
    httpd.serve_forever()

