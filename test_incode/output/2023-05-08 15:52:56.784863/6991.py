#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that converts fruits.txt to a json file
    server = HTTPServer(('', 8080), RequestHandler)
    server.serve_forever()

