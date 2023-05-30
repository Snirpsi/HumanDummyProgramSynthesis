#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that stores fruits.
    server = HTTPServer(("", 80), FruitHandler)
    print("Serving at http://127.0.0.1:80/fruits")
    server.serve_forever()

