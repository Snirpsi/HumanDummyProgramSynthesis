#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that requests fruits.
    server = HTTPServer(("", 80), FruitHandler)
    server.serve_forever()

