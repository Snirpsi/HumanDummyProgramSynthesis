#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that converts words.txt into HTML
    web = web.Application([
        (r'/', web.StaticFileHandler, {'path': './'}),
        (r'/words.txt', web.StaticFileHandler, {'path': './words.txt'}),
        (r'/words/(.*)', web.StaticFileHandler, {'path': './words/$1'})
    ])
    web.listen(8888)
    web.run(host='0.0.0.0', port=8888)

