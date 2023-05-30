#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that prints user input.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import parse_qs

    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            query = parse_qs(
                self.path.split('?')[1],
                keep_blank_values=True
            )
            query = dict(query)
            query['q'] = input('Enter a query: ')
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(
                '<html><head><title>User Input</title></head>'
                '<body><p>%s</p></body></html>' % query['q']
            )

    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Serving at http://%s:%s/' % (server_address[0], server_address[1]))
    httpd.serve_forever()

