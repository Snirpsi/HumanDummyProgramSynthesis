#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that removes a list of numbers.
    #It will also serve as a simple test harness for your webserver.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from socketserver import ThreadingMixIn
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(numbers)
    
    server = HTTPServer(('', 8080), RequestHandler)
    ThreadingMixIn.instance().start()
    server.serve_forever()

