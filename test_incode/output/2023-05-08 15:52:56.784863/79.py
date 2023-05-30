#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that removes fruits.
    server = BaseHTTPServer.HTTPServer(('', 8000), FruirHandler)
    server.serve_forever()

