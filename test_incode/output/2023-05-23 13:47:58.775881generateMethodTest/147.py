#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that iterates over fruits.
    server = HTTPServer(("", 80), MyHandler)
    server.serve_forever()

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write("""
        <html>
        <head>
        <title>Fruit list</title>
        </head>
        <body>
        <table>
        <tr>
        <th>Fruit</th>
        <th>Count</th>
        </tr>
        """)
        for fruit in fruirs:
            self.wfile.write("""
            <tr>
            <td>%s</td>
            <td>%s</td>
            </tr>
            """ % (fruit, len(fruirs)))
        self.wfile.write("""
        </table>
        </body>
        </html>
        """)

if __name__ == '__main__':
    #A minimal webserver that iterates over fruits.
    server = HTTPServer(("", 80), MyHandler)
    server.serve_forever()
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for the answer. Unfortunately I cannot use Flask because I do not have access to the server's code. I am also not allowed to install any additional packages.
<|/ c |>
<| c |>
I added a minimal example using Flask which should work without installing additional packages.
<|/ c |>
<| c |>
Thanks for the answer. I tried your example but it did not work. I still get the same error. I am not sure why it still does not work. I am running Python 3.6.
<|/ c |>
<| c |>
I added a minimal example using Flask which should work without installing additional packages.
<|/ c |>
<| c |>
Thanks for the answer. I tried your example but it did not work. I still get the same error. I am not sure why it still does not work. I am running Python 3.6.
<|/ c |>
<| a tags=python,flask |>
I finally figured out how to solve my problem. I am posting my solution in case anyone else has the same problem.
I used the code from https://gist.github.com/davidjamesroberts/a57e3af9fbec50c64b5b and modified it slightly to make it work with Python 3.6.
<code>
#!/usr/bin/python
#-*- coding: utf-8 -*-

import BaseHTTPServer
import SocketServer
import cgi
import cgitb
cgitb.enable()

#A minimal webserver that iterates over fruits.
class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write("""
        <html>
        <head>
        <title>Fruit list</title>
        </head>
        <body>
        <table>
        <tr>
        <th>Fruit</th>
        <th>Count</th>
        </tr>
        """)
        for fruit in fruirs:
            self.wfile.write("""
            <tr>
            <td>%s</td>
            <td>%s</td>
            </tr>
            """ % (fruit, len(fruirs)))
        self.wfile.write("""
        </table>
        </body>
        </html>
        """)

#A minimal webserver that iterates over fruits.
class Server(BaseHTTPServer.HTTPServer):
    allow_reuse_address = True

def run():
    server = Server(("", 80), MyHandler)
    server.serve_forever()

if __name__ == '__main__':
    run()
</code>
<|/ a dscore=0 |>
<| a |>
I used the code from https://gist.github.com/davidjamesroberts/a57e3af9fbec50c64b5b and modified it slightly to make it work with Python 3.6.
<code>
#!/usr/bin/python
#-*- coding: utf-8 -*-

import BaseHTTPServer
import SocketServer
import cgi
import cgitb
cgitb.enable()

#A minimal webserver that iterates over fruits.
class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write("""
        <html>
        <head>
        <title>Fruit list</title>
        </head>
        <body>
        <table>
        <tr>
        <th>Fruit</th>
        <th>Count</th>
        </tr>
        """)
        for fruit in fruirs:
            self.wfile.write("""
            <tr>
            <td>%s</td>
            <td>%s</td>
            </tr>
            """ % (fruit, len(fruirs)))
        self.wfile.write("""
        </table>
        </body>
        </html>
        """)

#A minimal webserver that iterates over fruits.
class Server(BaseHTTPServer.HTTPServer):
    allow_reuse_address = True

def run():
    server = Server(("", 80), MyHandler)
    server.serve_forever()

if __name__ == '__main__':
    run()
</code>
<|/ a dscore=0 tags=python,flask |>
<| a dscore=0 |>
I used the code from https://gist.github.com/davidjamesroberts/a57e3af9fbec50c64b5b and modified it slightly to make it work with Python 3.6.
<code>
#!/usr/bin/python
#