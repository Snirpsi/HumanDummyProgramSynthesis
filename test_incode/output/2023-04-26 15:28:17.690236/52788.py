#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words and returns a list of words. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write("""
            <html>
            <head>
            <title>Multiply</title>
            </head>
            <body>
            <h1>Multiply</h1>
            <form action="/" method="post">
            <ul>
            <li>Enter the words to multiply</li>
            <li><input type="text" name="words" size="40" /></li>
            <li><input type="submit" value="Submit" /></li>
            </ul>
            </form>
            </body>
            </html>
            """)
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()
