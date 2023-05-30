#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that converts fruits.txt to a json file
    server = HTTPServer(('', 8000), MyHandler)
    server.serve_forever()

