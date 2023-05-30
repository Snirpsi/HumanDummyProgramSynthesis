#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words. """    
    from http.server import BaseHTTPRequestHandler
    from urllib.parse import parse_qs
    import socketserver

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Get a query string and print it. """
            query = parse_qs(self.path.split('?')[1])
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(query['q'][0])

    httpd = socketserver.TCPServer(("", 80), Handler)
    print("serving at port", httpd.server_address[1])
    httpd.serve_forever()
</code>
<|/ a dscore=1 |>
<| c |>
Thanks for your answer. Could you please tell me how I can use your example to print words from a text file?
<|/ c |>
<| c |>
I added a small example to my answer. Hope it helps.
<|/ c |>
<| c |>
Thanks a lot! It works perfectly. Just one more question: how can I use your example to print words from a text file? I mean instead of printing them one by one like in my example above, I want to print them from a text file that contains the words. Could you please tell me how I can do that?
<|/ c |>
<| c |>
I added a small example to my answer. Hope it helps.
<|/ c |>
<| c |>
Thanks a lot! It works perfectly. Just one more question: how can I use your example to print words from a text file? I mean instead of printing them one by one like in my example above, I want to print them from a text file that contains the words. Could you please tell me how I can do that?
<|/ c |>
<| a tags=python,python-3.x,webserver |>
I wrote a small example to show how you can print words from a text file.
<code>
#!/usr/bin/env python3

import http.server
import socketserver

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        words = self.path.split('?')[1]
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(words)

if __name__ == "__main__":
    HOST, PORT = "localhost", 8000
    server = socketserver.TCPServer((HOST, PORT), Handler)
    server.serve_forever()
</code>
<|/ a dscore=1 |>
<| c |>
Thanks for your answer. Could you please tell me how I can use your example to print words from a text file?
<|/ c |>
<| c |>
I added a small example to 