#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that prints words.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse, parse_qs
    from socketserver import ThreadingMixIn
    from time import sleep

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            query = parse_qs(parsed_url.query)
            word = query["word"][0]
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(word, "utf8"))

    class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
        pass

    server_address = ('', 8080)
    httpd = ThreadedHTTPServer(server_address, Handler)
    httpd.serve_forever()

    #A minimal webserver that prints words and sleeps for 5 seconds.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse, parse_qs
    from socketserver import ThreadingMixIn
    from time import sleep

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            query = parse_qs(parsed_url.query)
            word = query["word"][0]
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(word, "utf8"))
            sleep(5)

    class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
        pass

    server_address = ('', 8080)
    httpd = ThreadedHTTPServer(server_address, Handler)
    httpd.serve_forever()
</code>
<|/ a dscore=2 |>
<| c |>
Thanks, this was very helpful. One question though: how would I go about making the server print out a message after each word is printed? For example, if the word "hello" is printed, then the server should print out a message saying "hello world!" after each word is printed.
<|/ c |>
<| c |>
I added a second example that prints words and sleeps for 5 seconds. You could also add an additional parameter to your handler that says how many words to print.
<|/ c |>
<| c |>
Thanks again, this is very helpful. One question though: how would I go about making the server print out a message after each word is printed? For example, if the word "hello" is printed, then the server should print out a message saying "hello world!" after each word is printed.
<|/ c |>
<| c |>
I added a second example that prints words and sleeps for 5 seconds. You could also add an additional parameter to your handler that says how many words to print.
<|/ c |>
<| c |>
Thanks again, this is very helpful. One question though: how would I go about making the server print out a message after each word is printed? For example, if the word "hello" is printed, then the server should print out a message saying "hello world!" after each word is printed.
<|/ c |>
<| a dscore=1 |>
<code>
#!/usr/bin/python3
import http.server
import urllib.parse
import urllib.request
import urllib.error
import socketserver

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed_url.query)
        word = query["word"][0]
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(word, "utf8"))

class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    pass

server_address = ('', 8080)
httpd = ThreadedHTTPServer(server_address, Handler)
httpd.serve_forever()
</code>
<|/ a tags=python,python-3.x,webserver |>
<| c |>
Thanks, this was very helpful. One question though: how would I go about making the server print out a message after each word is printed? For example, if the word "hello" is printed, then the server should print out a message saying "hello world!" after each word is printed.
<|/ c |>
<| c |>
I added a second example that prints words and sleeps for 5 seconds. You could also add an additional parameter to your handler that says how many words to print.
<|/ c |>
<| c |>
Thanks again, this is very helpful. One question though: how would I go about making the server print out a message after each word is printed? For example, if the word "hello" is printed, then the server should print out a message saying "hello world!" after each word is printed.
<|/ c |>
<| c |>
I added a second example that prints words and sleeps for 5 seconds. You could also add an additional parameter to your handler that says how many words to print.
<|/ c |>
<| a dscore=1 |>
<code>
#!/usr/bin/python3
import http.server
import urllib.parse
import urllib.request
import 