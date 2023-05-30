#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that adds fruits.
    server = HTTPServer(('', 8000), MyHandler)
    print('Serving at http://127.0.0.1:8000/')
    server.serve_forever()

