#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that opens fruits.html on port 8080
    server = HTTPServer(('', 8080), FruitHandler)
    server.serve_forever()

