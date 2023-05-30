#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that removes words.
    server = HTTPServer(('', 8000), MyHandler)
    print('Starting web server on port 8000...')
    server.serve_forever()

