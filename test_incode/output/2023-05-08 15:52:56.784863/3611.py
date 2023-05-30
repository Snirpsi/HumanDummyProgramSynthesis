#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that converts words.txt into html and serves it.
    web = web.application(
        web.url('/', IndexHandler),
        web.url('/words', WordsHandler),
        web.url('/words/<string:word>', WordHandler),
        web.url('/words/<string:word>/<string:format>', WordHandler),
        web.url('/words/<string:word>/<string:format>/<string:format>', WordHandler),
        web.url('/words/<string:word>/<string:format>/<string:format>/<string:format>', WordHandler),
        web.url('/words/<string:word>/<string:format>/<string:format>/<string:format>/<string:format>', WordHandler),
        web.url('/words/<string:word>/<string:format>/<string:format>/<string:format>/<string:format>', WordHandler),
        web.url('/words/<string:word>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>', WordHandler),
        web.url('/words/<string:word>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>', WordHandler),
        web.url('/words/<string:word>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>', WordHandler),
        web.url('/words/<string:word>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>', WordHandler),
        web.url('/words/<string:word>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>', WordHandler),
        web.url('/words/<string:word>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>', WordHandler),
        web.url('/words/<string:word>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>', WordHandler),
        web.url('/words/<string:word>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>', WordHandler),
        web.url('/words/<string:word>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>', WordHandler),
        web.url('/words/<string:word>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>', WordHandler),
        web.url('/words/<string:word>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>', WordHandler),
        web.url('/words/<string:word>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>', WordHandler),
        web.url('/words/<string:word>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>', WordHandler),
        web.url('/words/<string:word>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>', WordHandler),
        web.url('/words/<string:word>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>', WordHandler),
        web.url('/words/<string:word>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>', WordHandler),
        web.url('/words/<string:word>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>', WordHandler),
        web.url('/words/<string:word>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>', WordHandler),
        web.url('/words/<string:word>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>', WordHandler),
        web.url('/words/<string:word>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<string:format>/<

