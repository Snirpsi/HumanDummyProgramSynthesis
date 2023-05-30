#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port. """    
    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>Hello World!</h1>')
    
    httpd = HTTPServer(("", 8000), MyHandler)
    
    print("Serving at http://127.0.0.1:8000/")
    httpd.serve_forever()
    
