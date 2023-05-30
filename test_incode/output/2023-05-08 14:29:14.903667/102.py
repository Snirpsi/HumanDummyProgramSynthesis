#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that returns user input.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import parse_qs

    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            query = parse_qs(
                self.path.split('?')[1],
                keep_blank_values=True,
            )
            query = dict(query)
            query = query.get('q')
            if query:
                query = query.replace(' ', '+')
                self.wfile.write(
                    f'<html><head><title>Search Results for "{query}"</title></head>'
                    f'<body><p>{query}</p></body></html>'
                )
            else:
                self.wfile.write(
                    f'<html><head><title>Search Results for "No search terms found"</title></head>'
                    f'<body><p>No search terms found</p></body></html>'
                )

    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    httpd.serve_forever()

