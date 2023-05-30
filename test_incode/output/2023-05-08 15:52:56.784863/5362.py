#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that removes fruits.
    server = BaseHTTPServer.HTTPServer(('localhost', 8000), RequestHandler)
    server.serve_forever()

