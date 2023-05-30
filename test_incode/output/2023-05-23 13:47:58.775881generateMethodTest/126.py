#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A endless loop that opens all ports.
    while True:
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('0.0.0.0', port))
            sock.listen(1)
            print('Listening on port {}'.format(port))
            conn, addr = sock.accept()
            print('Connected by', addr)
            conn.settimeout(10)
            conn.send(b'Hello, world!')
            conn.close()
            sock.close()
</code>
<|/ a dscore=0 |>
<| c |>
This doesn't seem to work. I'm getting a timeout error when I try to connect to the server from the client side.
<|/ c |>
<| c |>
I added the client side code in the original post. Can you please take a look?
<|/ c |>
<| c |>
I added the client side code in the original post. Can you please take a look?
<|/ c |>
<| c |>
I added the client side code in the original post. Can you please take a look?
<|/ c |>
<| c |>
I added the client side code in the original post. Can you please take a look?
<|/ c |>
<| a tags=sockets,python,network-programming |>
The client side code looks fine, except that you are not closing the socket connection. Try adding conn.close() after conn.send(b'Hello, world!')
<|/ a dscore=0 |>
<| c |>
I added the client side code in the original post. Can you please take a look?
<|/ c |>
<| c |>
I added the client side code in the original post. Can you please take a look?
<|/ c |>
<| a dscore=0 |>
I added the client side code in the original post. Can you please take a look?

The client side code looks fine, except that you are not closing the socket connection. Try adding conn.close() after conn.send(b'Hello, world!')
<|/ a tags=sockets,python,network-programming |>
<| c |>
I added the client side code in the original post. Can you please take a look?
<|/ c |>
<| c |>
I added the client side code in the original post. Can you please take a look?
<|/ c |>
<| c |>
I added the client side code in the original post. Can you please take a look?
<|/ c |>
<| c |>
I added the client side code in the original post. Can you please take a look?
<|/ c |>
<| c |>
I added the client side code in the original post. Can you please take a look?
<|/ c |>
<| a tags=sockets,python,network-programming |>
I added the client side code in the original post. Can you please take a look?

The client side code looks fine, except that you are not closing the socket connection. Try adding conn.close() after conn.send(b'Hello, world!')
<|/ a dscore=0 |>
<| c |>
I added the client side code in the original post. Can you please take a look?
<|/ c |>
<| c |>
I added the client side code in the original post. Can you please take a look?
<|/ c |>
<| c |>
I added the client side code in the original post. Can you please take a look?
<|/ c |>
<| c |>
I added the client side code in the original post. Can you please take a look?
<|/ c |>
<| c |>
I added the client side code in the original post. Can you please take a look?
<|/ c |>
<| a tags=sockets,python,network-programming |>
I added the client side code in the original post. Can you please take a look?

The client side code looks fine, except that you are not closing the socket connection. Try adding conn.close() after conn.send(b'Hello, world!')
<|/ a dscore=0 |>
<| c |>
I added the client side code in the original post. Can you please take a look?
<|/ c |>
<| a tags=sockets,python,network-programming |>
I added the client side code in the original post. Can you please take a look?

The client side code looks fine, except that you are not closing the socket connection. Try adding conn.close() after conn.send(b'Hello, world!')
<|/ a dscore=0 |>
<| a tags=sockets,python,network-programming |>
I added the client side code in the original post. Can you please take a look?

The client side code looks fine, except that you are not closing the socket connection. Try adding conn.close() after conn.send(b'Hello, world!')
<|/ a dscore=0 |>
<| a dscore=0 |>
I added the client side code in the original post. Can you please take a look?

The client side code looks fine, except that you are not closing the socket connection. Try adding conn.close() after conn.send(b'Hello, world!')
<|/ a tags=