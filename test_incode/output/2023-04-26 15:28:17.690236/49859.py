#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits and opens a list of words. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write("""
            <html>
            <head>
            <title>Fruits</title>
            </head>
            <body>
            <ul>
            """)
            
            for fruit in fruits:
                self.wfile.write("""
                <li>%s</li>
                """ %fruit)
            
            self.wfile.write("""
            </ul>
            </body>
            </html>
            """)
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, FruitHandler)
    
    print('Starting server')
    httpd.serve_forever()
    
