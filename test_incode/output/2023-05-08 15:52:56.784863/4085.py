#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that opens words.txt and displays its content
    web = web.HTTPServer(('', 8000), web.RequestHandler)
    web.serve_forever()

