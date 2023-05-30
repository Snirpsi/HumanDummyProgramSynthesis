#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A endless loop that adds a port.
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        print('Listening on port ' + str(port))
        client, addr = sock.accept()
        print('Connected by', addr)
        while True:
            data = client.recv(1024)
            if not data:
                break
            client.send(data)
        print('Closing connection')
        client.close()
        sock.close()
</code>
<|/ a tags=python,sockets |>
<| c |>
Thanks for your answer. I am still new to socket programming, and I still don't know what to do. Could you please explain what to do? I tried to run your code, but I got this error: `File "server.py", line 13, in <module>
    sock.bind(('0.0.0.0', port))
socket.error: [Errno 98] Address already in use`
<|/ c |>
<| c |>
I ran the code again and now it works. Thanks a lot!
<|/ c |>
<| c |>
You're welcome. Glad I could help. I added some comments to help you understand what was going on. Good luck!
<|/ c |>
<| a tags=python,sockets |>
The error you are getting is because you are trying to bind the socket to 0.0.0.0:8080 which is already in use. 
The solution is to bind the socket to 0.0.0.0:8080 only once, before you try to bind to it again. 
<code>
import socket

port = 8080
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', port))
sock.listen(1)
print('Listening on port ' + str(port))
client, addr = sock.accept()
print('Connected by', addr)
while True:
    data = client.recv(1024)
    if not data:
        break
    client.send(data)
print('Closing connection')
client.close()
sock.close()
</code>
<|/ a dscore=2 |>
<| c |>
Thanks for your answer. I am still new to socket programming, and I still don't know what to do. Could you please explain what to do? I tried to run your code, but I got this error: `File "server.py", line 13, in <module>
    sock.bind(('0.0.0.0', port))
socket.error: [Errno 98] Address already in use`
<|/ c |>
<| c |>
I ran the code again and now it works. Thanks a lot!
<|/ c |>
<| a dscore=2 |>
The accepted answer works but if you want a more generic solution, you can use an event loop to listen for connections and then use that to send data back to the client:
<code>
import socket
import sys

port = 8080

def handle_connection(sock):
    while True:
        data = sock.recv(1024)
        if not data:
            break
        sock.send(data)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', port))
sock.listen(1)

print('Listening on port ' + str(port))
while True:
    client, addr = sock.accept()
    print('Connected by', addr)
    handle_connection(client)
</code>
<|/ a tags=python,sockets |>
<| a tags=python,sockets |>
The accepted answer works but if you want a more generic solution, you can use an event loop to listen for connections and then use that to send data back to the client:
<code>
import socket
import sys

port = 8080

def handle_connection(sock):
    while True:
        data = sock.recv(1024)
        if not data:
            break
        sock.send(data)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', port))
sock.listen(1)

print('Listening on port ' + str(port))
while True:
    client, addr = sock.accept()
    print('Connected by', addr)
    handle_connection(client)
</code>
<|/ a dscore=1 |>
<| a dscore=0 |>
I ran the code again and now it works. Thanks a lot!
<code>
import socket

port = 8080
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', port))
sock.listen(1)
print('Listening on port ' + str(port))
client, addr = sock.accept()
print('Connected by', addr)
while True:
    data = client.recv(1024)
    if not data:
        break
    client.send(data)
print('Closing connection')
client.close()
sock.close()
</code>
<|/ a tags=python,sockets |>
<| c |>
This code will never work. `bind` will fail if the port is already in use. `listen` will fail if the port is already in use. `accept` will fail if the port is already in use. `recv` will fail if the port is already in use. `send` will fail if the port is already in use. `bind` will fail if the port is already in use. `listen` will fail if the port is already in use. `accept` will fail if the port is already in use. `recv` will fail if the port is already in use. `send` will fail if the port is already in use. `bind` will fail if the port is already in use. `listen` will fail if the port is already in use. `accept` will fail if the port is already in use. `recv` will fail if the port is already 