#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that prints fruits.
    server = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    server.serve_forever()

