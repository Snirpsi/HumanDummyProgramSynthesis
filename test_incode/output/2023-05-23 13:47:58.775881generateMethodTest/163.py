#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A minimal webserver that opens all ports.
    httpd = HTTPServer(("", ports[0]), Handler)
    httpd.serve_forever()
</code>
<|/ a tags=python,sockets,webserver,python-3.x |>
<| c |>
Thank you very much! This was very helpful.
<|/ c |>
<| a dscore=0 |>
I wrote a small python script that does just that:
<code>
#!/usr/bin/env python3

import socket
import sys

HOST, PORT = "localhost", 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
print("Connected by", addr)
while True:
    data = conn.recv(1024)
    if not data:
        break
    print("Received", repr(data))
    conn.sendall(data)
conn.close()
</code>
It listens on port 9999 and accepts connections from any client on that port. It then sends back the data received.
<|/ a tags=python,sockets,webserver,python-3.x |>
<| c |>
Thank you very much! This was very helpful.
<|/ c |>
<| a tags=python,sockets,webserver,python-3.x |>
I wrote a small python script that does just that:
<code>
#!/usr/bin/env python3

import socket
import sys

HOST, PORT = "localhost", 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
print("Connected by", addr)
while True:
    data = conn.recv(1024)
    if not data:
        break
    print("Received", repr(data))
    conn.sendall(data)
conn.close()
</code>
It listens on port 9999 and accepts connections from any client on that port. It then sends back the data received.
<|/ a dscore=0 |>
<| a dscore=0 |>
<code>
import socket
import sys

HOST, PORT = "localhost", 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
print("Connected by", addr)
while True:
    data = conn.recv(1024)
    if not data:
        break
    print("Received", repr(data))
    conn.sendall(data)
conn.close()
</code>
<|/ a tags=python,sockets,webserver,python-3.x |>
<| c |>
Thank you very much! This was very helpful.
<|/ c |>
<| a dscore=0 |>
<code>
import socket
import sys

HOST, PORT = "localhost", 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
print("Connected by", addr)
while True:
    data = conn.recv(1024)
    if not data:
        break
    print("Received", repr(data))
    conn.sendall(data)
conn.close()
</code>
<|/ a tags=python,sockets,webserver,python-3.x |>
<| c |>
Thank you very much! This was very helpful.
<|/ c |>
<| a dscore=0 |>
<code>
import socket
import sys

HOST, PORT = "localhost", 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
print("Connected by", addr)
while True:
    data = conn.recv(1024)
    if not data:
        break
    print("Received", repr(data))
    conn.sendall(data)
conn.close()
</code>
<|/ a tags=python,sockets,webserver,python-3.x |>
<| a dscore=0 |>
<code>
import socket
import sys

HOST, PORT = "localhost", 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
print("Connected by", addr)
while True:
    data = conn.recv(1024)
    if not data:
        break
    print("Received", repr(data))
    conn.sendall(data)
conn.close()
</code>
<|/ a tags=python,sockets,webserver,python-3.x |>
<| c |>
Thank you very much! This was very helpful.
<|/ c |>
<| a dscore=0 |>
<code>
import socket
import sys

HOST, PORT = "localhost", 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
print("Connected by", addr)
while True:
    data = conn.recv(1024)
    if not data:
        break
    print("Received", repr(data))
    conn.sendall(data)
conn.close()
</code>
<|/ a tags=python,sockets,webserver,python-3.x |>
<| c |>
Thank you very much! This was very helpful.
<|/ c |>
<| a dscore=0 |>
<code>
import socket
import sys

HOST, PORT = "localhost", 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
print("Connected by", addr)
while True:
    data = conn.recv(1024)