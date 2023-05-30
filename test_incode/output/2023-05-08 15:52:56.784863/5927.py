#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that returns fruits.
    server = HTTPServer(('', 8000), MyHandler)
    print('Serving on port 8000...')
    server.serve_forever()

