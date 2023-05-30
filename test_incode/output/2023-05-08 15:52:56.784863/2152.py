#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that converts words.txt into html and serves it.
    httpd = HTTPServer(('', 8000), MyHandler)
    httpd.serve_forever()

