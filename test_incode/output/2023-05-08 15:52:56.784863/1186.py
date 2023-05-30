#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that converts numbers.txt into html
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import cgi
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            form = cgi.FieldStorage(
                fp=self.rfile, headers=self.headers,
                environ={'REQUEST_METHOD':'GET'})
            number = int(form['number'].value)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(str(number))
    server = HTTPServer(('', 8080), RequestHandler)
    server.serve_forever()

