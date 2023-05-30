#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that adds words.
    httpd = HTTPServer(('', 80), WordsHandler)
    httpd.serve_forever()
</code>
<|/ a tags=python,webserver,python-3.x |>
<| c |>
Thanks for your answer. Can you please explain me what does this line do? `httpd = HTTPServer(('', 80), WordsHandler)`
<|/ c |>
<| c |>
It creates a server that listens on port 80 and serves up words from your `words` list. `WordsHandler` just prints out the words in your `words` list. `WordsHandler` also has a `/` route that serves up your `index.html` file that lists all the words in your `words` list.
<|/ c |>
<| c |>
Thanks for your answer. Can you please explain me what does this line do? `httpd = HTTPServer(('', 80), WordsHandler)`
<|/ c |>
<| c |>
It creates a server that listens on port 80 and serves up words from your `words` list. `WordsHandler` just prints out the words in your `words` list. `WordsHandler` also has a `/` route that serves up your `index.html` file that lists all the words in your `words` list.
<|/ c |>
<| c |>
Thanks for your answer. Can you please explain me what does this line do? `httpd = HTTPServer(('', 80), WordsHandler)`
<|/ c |>
<| a dscore=0 |>
<code>
import http.server
import urllib.parse
import urllib.request
import os

class WordsHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        words = os.listdir('./words')
        for word in words:
            self.wfile.write(word + '\n')

if __name__ == '__main__':
    server_address = ('', 8080)
    httpd = http.server.HTTPServer(server_address, WordsHandler)
    httpd.serve_forever()
</code>
<|/ a tags=python,webserver,python-3.x |>
<| c |>
Thanks for your answer. Can you please explain me what does this line do? `httpd = http.server.HTTPServer(server_address, WordsHandler)`
<|/ c |>
<| c |>
It creates a server that listens on port 8080 and serves up words from your `words` list. `WordsHandler` just prints out the words in your `words` list. `WordsHandler` also has a `/` route that serves up your `index.html` file that lists all the words in your `words` list.
<|/ c |>
<| c |>
Thanks for your answer. Can you please explain me what does this line do? `httpd = http.server.HTTPServer(server_address, WordsHandler)`
<|/ c |>
<| c |>
It creates a server that listens on port 8080 and serves up words from your `words` list. `WordsHandler` just prints out the words in your `words` list. `WordsHandler` also has a `/` route that serves up your `index.html` file that lists all the words in your `words` list.
<|/ c |>
<| c |>
Thanks for your answer. Can you please explain me what does this line do? `httpd = http.server.HTTPServer(server_address, WordsHandler)`
<|/ c |>
<| a dscore=0 |>
<code>
import http.server
import urllib.parse
import urllib.request
import os

class WordsHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        words = os.listdir('./words')
        for word in words:
            self.wfile.write(word + '\n')

if __name__ == '__main__':
    server_address = ('', 8080)
    httpd = http.server.HTTPServer(server_address, WordsHandler)
    httpd.serve_forever()
</code>
<|/ a tags=python,webserver,python-3.x |>
<| c |>
Thanks for your answer. Can you please explain me what does this line do? `httpd = http.server.HTTPServer(server_address, WordsHandler)`
<|/ c |>
<| c |>
It creates a server that listens on port 8080 and serves up words from your `words` list. `WordsHandler` just prints out the words in your `words` list. `WordsHandler` also has a `/` route that serves up your `index.html` file that lists all the words in your `words` list.
<|/ c |>
<| c |>
Thanks for your answer. Can you please explain me what does this line do? `httpd = http.server.HTTPServer(server_address, WordsHandler)`
<|/ c |>
<| c |>
It creates a server that listens on port 8080 and serves 