#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that prints fruits.
    webserver = HTTPServer(('', 8080), FruitHandler)
    webserver.serve_forever()

