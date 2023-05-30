#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that removes fruits.
    server = HTTPServer(('', 8080), RequestHandler)
    server.serve_forever()

