#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that stores words.
    httpd = HTTPServer(('', 80), MyHandler)
    httpd.serve_forever()

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(words[0]))

if __name__ == '__main__':
    httpd = HTTPServer(('', 80), MyHandler)
    httpd.serve_forever()
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for your answer. Can you please explain me what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution and mine? I mean what is the difference between your solution