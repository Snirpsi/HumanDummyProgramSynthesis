#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A minimal webserver that stores all ports.
    server = HTTPServer(("", ports[0]), SimpleHTTPRequestHandler)
    print("Serving HTTP on port %d" % ports[0])
    server.serve_forever()
</code>
<|/ a tags=python,sockets,webserver |>
<| c |>
Thanks, this was very helpful.
<|/ c |>
<| a tags=python,sockets,webserver |>
<code>
import socket
import select
import webbrowser

PORT = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', PORT))
s.listen(1)

def handle_connection(conn):
    conn.send('HTTP/1.1 200 OK\r\n\r\nHello from Python!\r\n\r\n')
    conn.close()

while True:
    r, w, e = select.select([s], [], [])
    if r:
        conn, addr = s.accept()
        conn.setblocking(0)
        conn.settimeout(10)
        conn.send('HTTP/1.1 200 OK\r\n\r\nHello from Python!\r\n\r\n')
        conn.close()
        webbrowser.open('http://localhost:8000')
</code>
<|/ a dscore=4 |>
<| c |>
This code doesn't work if you try to open it from a browser. Try it yourself and you'll see what I mean.
<|/ c |>
<| c |>
This code doesn't work if you try to open it from a browser. Try it yourself and you'll see what I mean.
<|/ c |>
<| a tags=python,sockets,webserver |>
<code>
import socket
import select
import webbrowser

PORT = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', PORT))
s.listen(1)

def handle_connection(conn):
    conn.send('HTTP/1.1 200 OK\r\n\r\nHello from Python!\r\n\r\n')
    conn.close()

while True:
    r, w, e = select.select([s], [], [])
    if r:
        conn, addr = s.accept()
        conn.setblocking(0)
        conn.settimeout(10)
        conn.send('HTTP/1.1 200 OK\r\n\r\nHello from Python!\r\n\r\n')
        conn.close()
        webbrowser.open('http://localhost:8000')
</code>
<|/ a dscore=3 |>
<| c |>
This code doesn't work if you try to open it from a browser. Try it yourself and you'll see what I mean.
<|/ c |>
<| a tags=python,sockets,webserver |>
<code>
import socket
import select
import webbrowser

PORT = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', PORT))
s.listen(1)

def handle_connection(conn):
    conn.send('HTTP/1.1 200 OK\r\n\r\nHello from Python!\r\n\r\n')
    conn.close()

while True:
    r, w, e = select.select([s], [], [])
    if r:
        conn, addr = s.accept()
        conn.setblocking(0)
        conn.settimeout(10)
        conn.send('HTTP/1.1 200 OK\r\n\r\nHello from Python!\r\n\r\n')
        conn.close()
        webbrowser.open('http://localhost:8000')
</code>
<|/ a dscore=2 |>
<| a dscore=2 |>
<code>
import socket
import select
import webbrowser

PORT = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', PORT))
s.listen(1)

def handle_connection(conn):
    conn.send('HTTP/1.1 200 OK\r\n\r\nHello from Python!\r\n\r\n')
    conn.close()

while True:
    r, w, e = select.select([s], [], [])
    if r:
        conn, addr = s.accept()
        conn.setblocking(0)
        conn.settimeout(10)
        conn.send('HTTP/1.1 200 OK\r\n\r\nHello from Python!\r\n\r\n')
        conn.close()
        webbrowser.open('http://localhost:8000')
</code>
<|/ a tags=python,sockets,webserver |>
<| a dscore=2 |>
<code>
import socket
import select
import webbrowser

PORT = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', PORT))
s.listen(1)

def handle_connection(conn):
    conn.send('HTTP/1.1 200 OK\r\n\r\nHello from Python!\r\n\r\n')
    conn.close()

while True:
    r, w, e = select.select([s], [], [])
    if r:
        conn, addr = s.accept()
        conn.setblocking(0)
        conn.settimeout(10)
        conn.send('HTTP/1.1 200 OK\r\n\r\nHello from Python!\r\n\r\n')
        conn.close()
        webbrowser.open('http://localhost:8000')
</code>
<|/ a tags=python,sockets,webserver |>
<| a dscore=2 |>
<code>
import socket
import select
import webbrowser

PORT = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', PORT))
s.listen(1)

def handle_connection(conn):
    conn.send('HTTP/1.1 200 OK\r\n\r\nHello from Python!\r\n\r\n')
    conn.close()

while True:
    r, w, e = select.select([s], [], [])
    if r:
        conn, addr = s.accept()
