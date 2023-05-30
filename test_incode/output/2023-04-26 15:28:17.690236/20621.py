#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class WordListHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write("""
            <!DOCTYPE html>
            <html>
            <head>
            <title>Word List</title>
            </head>
            <body>
            <ul>
            """)
            
            for word in self.server.words:
                self.wfile.write("""
                <li>%s</li>
                """ % word)
            
            self.wfile.write("""
            </ul>
            </body>
            </html>
            """)
            
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, WordListHandler)
    
    print('Starting server')
    httpd.serve_forever()
    
