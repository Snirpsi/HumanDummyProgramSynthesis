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
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
            conn.close()
        ports = ports[1:] + ports[:1]
</code>
<|/ a tags=sockets,python,python-3.x |>
<| c |>
Thanks for your answer. Can you please explain what does this line do? `for port in ports:`
<|/ c |>
<| c |>
It loops through all ports available on the local machine. `ports` will contain all available ports. `for port in ports:` loops through all ports available on the local machine.
<|/ c |>
<| c |>
I understand that but why does it not work when I run it on my server?
<|/ c |>
<| c |>
It works fine on my server. Are you sure you have the correct port number?
<|/ c |>
<| c |>
Yes, I do have correct port number. I am running it on port 8080
<|/ c |>
<| a dscore=0 |>
I ran your code on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and it works fine. 
I ran it on my server and 