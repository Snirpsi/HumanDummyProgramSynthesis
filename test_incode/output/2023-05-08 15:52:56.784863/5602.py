#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that enumerates fruits.
    server = HTTPServer(('', 80), MyHandler)
    server.serve_forever()

