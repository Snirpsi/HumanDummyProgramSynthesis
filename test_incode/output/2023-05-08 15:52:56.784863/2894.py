#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that opens words.txt and displays its contents
    web = web.Application([
        (r'/', web.StaticFileHandler, {'path': os.path.dirname(__file__)}),
        (r'/words.txt', web.StaticFileHandler, {'path': os.path.dirname(__file__)}),
        (r'/words/(.*)', web.StaticFileHandler, {'path': os.path.dirname(__file__)}),
    ])
    web.listen(8080)
    web.run(host='0.0.0.0', port=8080)

