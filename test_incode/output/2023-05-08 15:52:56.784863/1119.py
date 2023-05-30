#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that prints a list of words.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    httpd = HTTPServer(("", 80), MyHandler)
    print("Starting httpserver on port 80")
    httpd.serve_forever()

