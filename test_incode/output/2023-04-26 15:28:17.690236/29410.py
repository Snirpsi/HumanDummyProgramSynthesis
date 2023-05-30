#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers and enumerates words. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import socketserver

    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            if self.path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write("""<html><body>
                    <h1>Enumerate Words</h1>
                    <p>
                        This page enumerates all words in the dictionary.
                    </p>
                    <p>
                        <a href="./index.html">Go back to the main page</a>
                    </p>
                    <p>
                        <a href="./dictionary.html">Go back to the dictionary</a>
                    </p>
                    <p>
                        <a href="./index.html">Exit</a>
                    </p>
                </body></html>""")
                return

            words = open('./words.txt').read().splitlines()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write("""<html><body>
                <h1>Enumerate Words</h1>
                <p>
                    This page enumerates all words in the dictionary.
                </p>
                <p>
                    <a href="./index.html">Go back to the main page</a>
                </p>
                <p>
                    <a href="./dictionary.html">Go back to the dictionary</a>
                </p>
                <p>
                    <a href="./index.html">Exit</a>
                </p>
            </body></html>""")
            for word in words:
                self.wfile.write('<p>%s</p>\n' % word)

    httpd = HTTPServer(("", 80), RequestHandler)
    httpd.serve_forever()
