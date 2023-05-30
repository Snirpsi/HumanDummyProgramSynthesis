#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that adds words.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from socketserver import ThreadingMixIn
    from time import sleep
    from random import randint
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == "/":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes("""
                    <html>
                    <head>
                    <title>Hello World</title>
                    </head>
                    <body>
                    <h1>Hello World</h1>
                    </body>
                    </html>
                """, "utf8"))
            else:
                word = parsed_url.path.split("/")[-1]
                
                if word in words:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(bytes("""
                        <html>
                        <head>
                        <title>Hello %s</title>
                        </head>
                        <body>
                        <h1>Hello %s</h1>
                        </body>
                        </html>
                    """ % (word, word), "utf8"))
                else:
                    self.send_response(404)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(bytes("""
                        <html>
                        <head>
                        <title>Not Found</title>
                        </head>
                        <body>
                        <h1>Not Found</h1>
                        </body>
                        </html>
                    """, "utf8"))
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    
    print("Starting web server on port 8080")
    httpd.serve_forever()
    
    #A minimal webserver that adds words.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from socketserver import ThreadingMixIn
    from time import sleep
    from random import randint
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == "/":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes("""
                    <html>
                    <head>
                    <title>Hello World</title>
                    </head>
                    <body>
                    <h1>Hello World</h1>
                    </body>
                    </html>
                """, "utf8"))
            else:
                word = parsed_url.path.split("/")[-1]
                
                if word in words:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(bytes("""
                        <html>
                        <head>
                        <title>Hello %s</title>
                        </head>
                        <body>
                        <h1>Hello %s</h1>
                        </body>
                        </html>
                    """ % (word, word), "utf8"))
                else:
                    self.send_response(404)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(bytes("""
                        <html>
                        <head>
                        <title>Not Found</title>
                        </head>
                        <body>
                        <h1>Not Found</h1>
                        </body>
                        </html>
                    """, "utf8"))
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    
    print("Starting web server on port 8080")
    httpd.serve_forever()
    
    #A minimal webserver that adds words.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from socketserver import ThreadingMixIn
    from time import sleep
    from random import randint
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == "/":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes("""
                    <html>
                    <head>
                    <title>Hello World</title>
                    </head>
                    <body>
                    <h1>Hello World</h1>
                    </body>
                    </html>
                """, "utf8"))
            else:
                word = parsed_url.path.split("/")[-1]
                
                if word in words:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(bytes("""
                        <html>
                        <head>
                        <title>Hello %s</title>
                        </head>
                        <body>
                        <h1>Hello %s</h1>
                        </body>
                        </html>
                    """ % (word, word), "utf8"))
                else:
                    self.send_response(404)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(bytes("""
                        <html>
                        <head>
                        <title>Not Found</title>
                        </head>
                        <body>
                        <h1>Not Found</h1>
                        </body>
                        </html>
                    """, "utf8"))
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    
    print("Starting web server on port 8080")
    httpd.serve_forever()
    
    #A minimal webserver that adds words.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from socketserver import ThreadingMixIn
    from time import sleep
    from random import randint
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.