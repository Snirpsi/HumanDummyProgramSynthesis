#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that opens words.txt and displays it
    web = web.HTTPServer(('', 8000), web.RequestHandler)
    web.serve_forever()

