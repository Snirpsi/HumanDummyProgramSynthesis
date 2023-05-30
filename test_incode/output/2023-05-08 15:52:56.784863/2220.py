#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that converts words.txt into HTML
    web = web.application(web.wsgifuncs, globals())
    web.run()

