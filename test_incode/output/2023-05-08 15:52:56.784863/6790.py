#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that calculates user input.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import parse_qs

    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            q = parse_qs(
                self.headers['QUERY_STRING'],
                keep_blank_values=True
            )
            answer = q['answer'][0]
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(answer)

    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()

