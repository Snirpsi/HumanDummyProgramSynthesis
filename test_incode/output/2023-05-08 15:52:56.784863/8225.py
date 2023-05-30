#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that opens a list of words.
    web = web.application(urls, globals())
    web.run()

