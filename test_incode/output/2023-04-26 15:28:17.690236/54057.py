#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes all ports. """    
    ports = range(65535)
    while True:
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('0.0.0.0', port))
            sock.listen(1)
            sock.close()
        ports.remove(65535)
        time.sleep(1)
</code>
<|/ a dscore=0 |>
<| c |>
This doesn't work. `sock.close()` will cause the program to crash.
<|/ c |>
<| c |>
I 