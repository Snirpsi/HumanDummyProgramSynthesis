#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that opens fruits.txt and displays them in HTML
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    import io
    import os
    import random
    
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
                <title>Fruits</title>
                </head>
                <body>
                """)
                for fruit in fruirs:
                    self.wfile.write("""
                    <p>%s</p>
                    """ % fruit)
                self.wfile.write("""
                </body>
                </html>
                """)
            elif path == "/fruits.txt":
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write("""
                Fruits:
                apple
                banana
                orange
                """)
            elif path == "/fruits.txt?random":
                f = io.StringIO()
                random.shuffle(fruirs)
                f.writelines(fruirs)
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(f.getvalue())
            elif path == "/fruits.txt?random&fruits=1":
                f = io.StringIO()
                random.shuffle(fruirs)
                f.writelines(fruirs)
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(f.getvalue())
            elif path == "/fruits.txt?random&fruits=2":
                f = io.StringIO()
                random.shuffle(fruirs)
                f.writelines(fruirs)
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(f.getvalue())
            elif path == "/fruits.txt?random&fruits=3":
                f = io.StringIO()
                random.shuffle(fruirs)
                f.writelines(fruirs)
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(f.getvalue())
            elif path == "/fruits.txt?random&fruits=4":
                f = io.StringIO()
                random.shuffle(fruirs)
                f.writelines(fruirs)
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(f.getvalue())
            elif path == "/fruits.txt?random&fruits=5":
                f = io.StringIO()
                random.shuffle(fruirs)
                f.writelines(fruirs)
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(f.getvalue())
            elif path == "/fruits.txt?random&fruits=6":
                f = io.StringIO()
                random.shuffle(fruirs)
                f.writelines(fruirs)
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(f.getvalue())
            elif path == "/fruits.txt?random&fruits=7":
                f = io.StringIO()
                random.shuffle(fruirs)
                f.writelines(fruirs)
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(f.getvalue())
            elif path == "/fruits.txt?random&fruits=8":
                f = io.StringIO()
                random.shuffle(fruirs)
                f.writelines(fruirs)
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(f.getvalue())
            elif path == "/fruits.txt?random&fruits=9":
                f = io.StringIO()
                random.shuffle(fruirs)
                f.writelines(fruirs)
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(f.getvalue())
            elif path == "/fruits.txt?random&fruits=10":
                f = io.StringIO()
                random.shuffle(fruirs)
                f.writelines(fruirs)
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(f.getvalue())
            elif path == "/fruits.txt?random&fruits=11":
                f = io.StringIO()
                random.shuffle(fruirs)
                f.writelines(fruirs)
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(f.getvalue())
            elif path == "/fruits.txt?random&fruits=12":
                f = io.StringIO()
                random.shuffle(fruirs)
                f.writelines(fruirs)
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(f.getvalue())
            elif path == "/fruits.txt?random&fruits=13":
                f = io.StringIO()
                random.shuffle(fruirs)