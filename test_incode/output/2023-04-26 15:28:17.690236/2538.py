#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write("""<html><body>
                <h1>List of numbers</h1>
                <ul>
                    """)
            for num in range(1,11):
                self.wfile.write("""<li>%s</li>\n""" % num)
            self.wfile.write("""</ul>
            </body></html>""")
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    
    print('Starting httpserver on port 8080')
    httpd.serve_forever()
    
