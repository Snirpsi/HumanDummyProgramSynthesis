#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A minimal webserver that stores a port.
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    server.serve_forever()
</code>
<|/ a dscore=1 |>
<| c |>
Thanks for your answer. Unfortunately this doesn't work for me. I'm running this on a raspberry pi 3 with python 3.7 and it just hangs. I edited my question to include my full code.
<|/ c |>
<| c |>
I added a minimal example that works on my machine. Can you try it on your machine?
<|/ c |>
<| c |>
I added the full code to the question. Unfortunately it still doesn't work. I'm running this on a raspberry pi 3 with python 3.7 and it just hangs. I edited my question to include my full code.
<|/ c |>
<| c |>
I added a minimal example that works on my machine. Can you try it on your machine?
<|/ c |>
<| c |>
I added the full code to the question. Unfortunately it still doesn't work. I'm running this on a raspberry pi 3 with python 3.7 and it just hangs. I edited my question to include my full code.
<|/ c |>
<| a tags=python,raspberry-pi3,raspbian |>
I finally found a solution to my problem. 
I used the code from https://gist.github.com/jamesross/a447d1fb34d67e3be7a
I added the code below to my python script:
<code>
import http.server
import socketserver
import SimpleHTTPServer
import SocketServer

PORT = 8080

class SimpleHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes('<html><head><title>Hello World</title></head><body>Hello World</body></html>', 'UTF-8'))

server = SocketServer.TCPServer(("", PORT), SimpleHTTPRequestHandler)
print("serving at port", PORT)
server.serve_forever()
</code>
I then ran the script on my raspberry pi 3 with python 3.7 and it worked. 
I hope this helps anyone else who has the same problem.
<|/ a dscore=1 |>
<| a dscore=0 |>
I used the code from https://gist.github.com/jamesross/a447d1fb34d67e3be7a
I added the code below to my python script:
<code>
import http.server
import socketserver
import SimpleHTTPServer
import SocketServer

PORT = 8080

class SimpleHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes('<html><head><title>Hello World</title></head><body>Hello World</body></html>', 'UTF-8'))

server = SocketServer.TCPServer(("", PORT), SimpleHTTPRequestHandler)
print("serving at port", PORT)
server.serve_forever()
</code>
I then ran the script on my raspberry pi 3 with python 3.7 and it worked. 
I hope this helps anyone else who has the same problem.
<|/ a tags=python,raspberry-pi3,raspbian |>
<| c |>
This doesn't work for me. I'm running this on a raspberry pi 3 with python 3.7 and it just hangs. I edited my question to include my full code.
<|/ c |>
<| a |>
I used the code from https://gist.github.com/jamesross/a447d1fb34d67e3be7a
I added the code below to my python script:
<code>
import http.server
import socketserver
import SimpleHTTPServer
import SocketServer

PORT = 8080

class SimpleHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes('<html><head><title>Hello World</title></head><body>Hello World</body></html>', 'UTF-8'))

server = SocketServer.TCPServer(("", PORT), SimpleHTTPRequestHandler)
print("serving at port", PORT)
server.serve_forever()
</code>
I then ran the script on my raspberry pi 3 with python 3.7 and it worked. 
I hope this helps anyone else who has the same problem.
<|/ a dscore=0 tags=python,raspberry-pi3,raspbian |>
<| a dscore=0 |>
I used the code from https://gist.github.com/jamesross/a447d1fb34d67e3be7a
I added the code below to my python script:
<code>
import http.server
import socketserver
import SimpleHTTPServer
import SocketServer

PORT = 8080

class SimpleHTTPRequestHandler(SimpleHTTP