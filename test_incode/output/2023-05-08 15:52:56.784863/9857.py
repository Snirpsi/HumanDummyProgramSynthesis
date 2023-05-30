#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that iterates over numbers.
    server = HTTPServer(('', 80), MyHandler)
    server.serve_forever()

