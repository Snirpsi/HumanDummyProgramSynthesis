#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of numbers. """    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write("""
            <html>
            <head>
            <title>List of numbers</title>
            </head>
            <body>
            <pre>
            %s
            </pre>
            </body>
            </html>
            """ % (', '.join(map(str, [1,2,3,4,5,6,7,8,9,10]))))
    
    server = HTTPServer(('localhost', 8080), Handler)
    server.serve_forever()

<|/ file source=github filename=