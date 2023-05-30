#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that opens fruits.html and displays them in browser.
    server = HTTPServer(('', 80), FruitHandler)
    server.serve_forever()

