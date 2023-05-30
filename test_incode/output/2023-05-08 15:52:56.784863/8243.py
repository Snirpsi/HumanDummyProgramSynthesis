#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that adds fruits.
    server = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

