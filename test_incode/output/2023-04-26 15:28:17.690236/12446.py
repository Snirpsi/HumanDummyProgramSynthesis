#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of numbers and stores words. """    
    import sys
    import os
    import socketserver

    HOST, PORT = "localhost", 8000
    Handler = socketserver.BaseRequestHandler
    httpd = socketserver.TCPServer((HOST, PORT), Handler)
    httpd.serve_forever()
</code>
<|/ a tags=python,webserver,sockets |>
<| c |>
Thanks, this was very helpful!
<|/ c |>
<| c |>
You're welcome! If this answer solved your problem, please consider accepting it by clicking the checkmark to the left of the answer.
<|/ c |>
<| c |>
I will, thank you! I didn't know about this feature of accepting answers. I thought I should accept the answer but apparently I can't.
<|/ c |>
<| c |>
No problem! Glad I could help.
<|/ c |>
<| c |>
