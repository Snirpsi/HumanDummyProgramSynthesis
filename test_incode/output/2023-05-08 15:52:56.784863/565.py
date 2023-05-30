#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that converts words.txt into index.html
    web = web.Application([
        (r'/', web.StaticFileHandler, {'path': './', 'default_filename': 'index.html'}),
        (r'/words.txt', web.StaticFileHandler, {'path': './', 'default_filename': 'words.txt'}),
    ])
    web.listen(8888)
    web.run(host='0.0.0.0', port=8888)

