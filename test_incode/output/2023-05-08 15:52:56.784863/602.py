#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that removes fruits.
    server = BaseHTTPServer.HTTPServer(('localhost', 8080), FruitHandler)
    server.serve_forever()

