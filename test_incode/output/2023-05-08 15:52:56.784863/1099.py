#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that requests fruits.
    server = HTTPServer(("localhost", 8080), FruitHandler)
    print("Serving on port 8080")
    server.serve_forever()

