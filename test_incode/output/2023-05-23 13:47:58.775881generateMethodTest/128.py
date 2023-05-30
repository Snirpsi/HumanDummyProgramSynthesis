#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that adds fruits.
    import os
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    import random
    import json
    import cgi
    
    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = urlparse(self.path).path
            if path == "/":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write("""
                <html>
                <head>
                <title>Fruit List</title>
                </head>
                <body>
                <h1>Fruit List</h1>
                <ul>
                """)
                for fruit in fruirs:
                    self.wfile.write("""
                    <li>%s</li>
                    """ % fruit)
                self.wfile.write("""
                </ul>
                </body>
                </html>
                """)
            else:
                path = "/" + path
                if path == "/add":
                    form = cgi.FieldStorage(
                        fp=self.rfile,
                        headers=self.headers,
                        environ={'REQUEST_METHOD':'POST'})
                    name = form.getvalue('name')
                    fruit = form.getvalue('fruit')
                    
                    fruirs.append(fruit)
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write("""
                    <html>
                    <head>
                    <title>Fruit Added</title>
                    </head>
                    <body>
                    <h1>Fruit Added</h1>
                    <p>Name: <b>%s</b> </p>
                    <p>Fruit: <b>%s</b> </p>
                    </body>
                    </html>
                    """ % (name, fruit, fruit))
                elif path == "/remove":
                    form = cgi.FieldStorage(
                        fp=self.rfile,
                        headers=self.headers,
                        environ={'REQUEST_METHOD':'POST'})
                    name = form.getvalue('name')
                    fruit = form.getvalue('fruit')
                    
                    fruirs.remove(name)
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write("""
                    <html>
                    <head>
                    <title>Fruit Removed</title>
                    </head>
                    <body>
                    <h1>Fruit Removed</h1>
                    <p>Name: <b>%s</b> </p>
                    <p>Fruit: <b>%s</b> </p>
                    </body>
                    </html>
                    """ % (name, fruit, fruit))
                elif path == "/update":
                    form = cgi.FieldStorage(
                        fp=self.rfile,
                        headers=self.headers,
                        environ={'REQUEST_METHOD':'POST'})
                    name = form.getvalue('name')
                    fruit = form.getvalue('fruit')
                    
                    fruirs[name]=fruit
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write("""
                    <html>
                    <head>
                    <title>Fruit Updated</title>
                    </head>
                    <body>
                    <h1>Fruit Updated</h1>
                    <p>Name: <b>%s</b> </p>
                    <p>Fruit: <b>%s</b> </p>
                    </body>
                    </html>
                    """ % (name, fruit, fruit))
                elif path == "/delete":
                    form = cgi.FieldStorage(
                        fp=self.rfile,
                        headers=self.headers,
                        environ={'REQUEST_METHOD':'POST'})
                    name = form.getvalue('name')
                    fruit = form.getvalue('fruit')
                    
                    fruirs.pop(name)
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write("""
                    <html>
                    <head>
                    <title>Fruit Deleted</title>
                    </head>
                    <body>
                    <h1>Fruit Deleted</h1>
                    <p>Name: <b>%s</b> </p>
                    <p>Fruit: <b>%s</b> </p>
                    </body>
                    </html>
                    """ % (name, fruit, fruit))
                else:
                    self.send_error(404)
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, FruitHandler)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
