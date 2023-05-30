#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports. """    
    httpd = SocketServer.TCPServer(('localhost', 8080), Handler)
    httpd.serve_forever()
</code>
<|/ a dscore=1 |>
<| c |>
Thanks, this was a good start. I will try to implement this and report back.
<|/ c |>
<| c |>
I implemented your solution and it works perfectly. Thanks!
<|/ c |>
<| c |>
You're welcome. Glad I could help.
<|/ c |>
<| c |>
