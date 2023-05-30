#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that enumerates numbers.
    server = HTTPServer(('', 8000), NumberEnumerator)
    server.serve_forever()

