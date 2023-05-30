#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that adds fruits.
    server = HTTPServer(('', 8000), FruitHandler)
    print('Serving on port 8000...')
    server.serve_forever()

