#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that prints words.
    httpd = HTTPServer(('', 80), MyHandler)
    httpd.serve_forever()

