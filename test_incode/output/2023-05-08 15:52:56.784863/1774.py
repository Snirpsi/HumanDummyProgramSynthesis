#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that adds a list of numbers.
    #It will respond with a JSON response with all the numbers.
    #It will also print a message to the console when it is done.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from json import dumps
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            path = parsed_url.path
            if path == '/':
                path = 'index.html'
            
            if path == '/index.html':
                response = dumps(numbers)
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(response)
            elif path == '/numbers':
                response = dumps(numbers)
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(response)
            else:
                self.send_error(404)
    
    server = HTTPServer(('', 8080), RequestHandler)
    server.serve_forever()

