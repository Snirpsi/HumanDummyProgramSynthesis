#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that returns fruits.
    import os
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    import socketserver
    import random
    
    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = urlparse(self.path).path
            if path == "/":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(open("index.html").read())
            elif path == "/fruit":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(open("fruit.html").read())
            elif path == "/fruit/random":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(open("fruit.random").read())
            elif path == "/fruit/random/1":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(open("fruit.random").read())
            elif path == "/fruit/random/2":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(open("fruit.random").read())
            elif path == "/fruit/random/3":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(open("fruit.random").read())
            elif path == "/fruit/random/4":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(open("fruit.random").read())
            elif path == "/fruit/random/5":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(open("fruit.random").read())
            elif path == "/fruit/random/6":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(open("fruit.random").read())
            elif path == "/fruit/random/7":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(open("fruit.random").read())
            elif path == "/fruit/random/8":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(open("fruit.random").read())
            elif path == "/fruit/random/9":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(open("fruit.random").read())
            elif path == "/fruit/random/10":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(open("fruit.random").read())
            elif path == "/fruit/random/11":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(open("fruit.random").read())
            elif path == "/fruit/random/12":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(open("fruit.random").read())
            elif path == "/fruit/random/13":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(open("fruit.random").read())
            elif path == "/fruit/random/14":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(open("fruit.random").read())
            elif path == "/fruit/random/15":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(open("fruit.random").read())
            elif path == "/fruit/random/16":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(open("fruit.random").read())
            elif path == "/fruit/random/17":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(open("fruit.random").read())
            elif path == "/fruit/random/18":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(open("fruit.random").read())
            elif path == "/fruit/random/19":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(open("fruit.random").read())
            elif path == "/fruit/random/20":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(open("fruit.random").read())
            elif path == "/fruit/random/21":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(open("fruit.random").read())
            elif path == "/fruit/random/22":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.