#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that requests words.txt and prints them back
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    import socketserver

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = urlparse(self.path).path
            if path == "/":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes("""
                <html>
                <body>
                <h1>Hello World!</h1>
                </body>
                </html>
                """, "utf-8"))
            elif path == "/words.txt":
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(bytes("""
                hello
                world
                !
                """, "utf-8"))
            else:
                self.send_error(404)
                self.end_headers()

    server_address = ('', 8080)
    httpd = HTTPServer(server_address, Handler)
    httpd.serve_forever()

#EOF

#
# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
#
# vim: set ts=4 sw=4 et tw=79 fdm=indent:
#
# vim: set ts=4 sw=4 et tw=79 fdm=indent:
#
# vim: set ts=4 sw=4 et tw=79 fdm=indent:
#
# vim: set ts=4 sw=4 et tw=79 fdm=indent:
#
# vim: set ts=4 sw=4 et tw=79 fdm=indent:
#
# vim: set ts=4 sw=4 et tw=79 fdm=indent:
#
# vim: set ts=4 sw=4 et tw=79 fdm=indent:
#
# vim: set ts=4 sw=4 et tw=79 fdm=indent:
#
# vim: set ts=4 sw=4 et tw=79 fdm=indent:
#
# vim: set ts=4 sw=4 et tw=79 fdm=indent:
#
# vim: set ts=4 sw=4 et tw=79 fdm=indent:
#
# vim: set ts=4 sw=4 et tw=79 fdm=indent:
#
# vim: set ts=4 sw=4 et tw=79 fdm=indent:
#
# vim: set ts=4 sw=4 et tw=79 fdm=indent:
#
# vim: set ts=4 sw=4 et tw=79 fdm=indent:
#
# vim: set ts=4 sw=4 et tw=79 fdm=indent:
#
# vim: set ts=4 sw=4 et tw=79 fdm=indent:
#
# vim: set ts=4 sw=4 et tw=79 fdm=indent:
#
# vim: set ts=4 sw=4 et tw=79 fdm=indent:
#
# vim: set ts=4 sw=4 et tw=79 fdm=indent:
#
# vim: set ts=4 sw=4 et tw=79 fdm=indent:
#
# vim: set ts=4 sw=4 et tw=79 fdm=indent:
#
# vim: set ts=4 sw=4 et tw=79 fdm=indent:
#
# vim: set ts=4 sw=4 et tw=79 fdm=indent:
#
# vim: set ts=4 sw=4 et tw=79 fdm=indent:
#
# vim: set ts=4 sw=4 et tw=79 fdm=indent:
#
# vim: set ts=4 sw=4 et tw=79 fdm=indent:
#
# vim: set ts=4 sw=4 et tw=79 fdm=indent:
#
# vim: set ts=4 sw=4 et tw=79 fdm=indent:
#
# vim: set ts=4 sw=4 et tw=79 fdm=indent:
#
# vim: set ts=4 sw=4 et tw=79 fdm=indent:
#
# vim: set ts=4 sw=4 et tw=79 fdm=indent:
#
# vim: set ts=4 sw=4 et tw=79 fdm=indent:
#
# vim: set ts=4 sw=4 et tw=79 fdm=indent:
#
# vim: set ts=4 sw=4 et tw=79 fdm=indent:
#
# vim: set t