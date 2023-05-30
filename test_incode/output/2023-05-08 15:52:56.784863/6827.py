#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that opens fruits.txt and displays it.
    webserver = HTTPServer(('', 80), FruitHandler)
    webserver.serve_forever()

