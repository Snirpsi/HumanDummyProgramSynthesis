#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that converts a list of words.
    #It will listen on port 8000 and convert each word in the list to uppercase.
    #It will also print a message to the console each time a word is converted.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from socketserver import ThreadingMixIn
    from threading import Thread

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            words = parsed_url.path.split('/')
            words = [word.upper() for word in words]
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(
                '<html><head><title>Converting Words</title></head>'
                '<body><p>Converting Words</p>'
                '<ol>%s</ol></body></html>'
                % '\n'.join(words),
                'utf8'))

    class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
        pass

    server_address = ('', 8000)
    httpd = ThreadedHTTPServer(server_address, Handler)
    httpd.serve_forever()

