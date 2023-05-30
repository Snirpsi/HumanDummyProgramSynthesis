#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that opens words.txt and displays its content
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from io import BytesIO
    from urllib.parse import urlparse, parse_qs

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = urlparse(self.path).path
            if path == "/":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes(open(words[0], "r").read()))
            elif path == "/words":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes(open(words[1], "r").read()))
            elif path == "/words/":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes(open(words[2], "r").read()))
            else:
                self.send_error(404)
                self.end_headers()

    server_address = ('', 8080)
    httpd = HTTPServer(server_address, Handler)
    httpd.serve_forever()
</code>
<|/ a tags=python,html,flask |>
<| c |>
Thanks for your answer. I am not familiar with flask but I am going to try it out. Thanks again.
<|/ c |>
<| c |>
I added a flask example to my answer
<|/ c |>
<| c |>
Thanks for your answer. I am not familiar with flask but I am going to try it out. Thanks again.
<|/ c |>
<| a tags=python,html,flask |>
I used flask to create a web page that displays words from a text file. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I used a for loop to display the words. I 