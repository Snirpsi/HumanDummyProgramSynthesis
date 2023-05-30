#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port. """    
    port = 8080
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    httpd.serve_forever()
</code>
<|/ a |>
<| c |>
Thanks for your answer. Unfortunately this doesn't solve my problem because I need the port to be accessible from the outside world.
<|/ c |>
<| c |>
I added a working example that uses `socket.gethostname()` to get the host name.
<|/ c |>
<| c |>
Thanks for your answer. Unfortunately this doesn't solve my problem because I need the port to be accessible from the outside world.
<|/ c |>
<| c |>
I added a working example that uses `socket.gethostname()` to get the host name.
<|/ c |>
<| c |>
Thanks for your answer. Unfortunately this doesn't solve my problem because I need the port to be accessible from the outside world.
<|/ c |>
<| a tags=python,webserver,sockets |>
I used this code to solve my problem:
<code>
import socket
import http.server

HOST, PORT = "localhost", 8080
Handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer( (HOST, PORT), Handler )
httpd.serve_forever()
</code>
<|/ a dscore=0 |>
<| c |>
Please don't post only code as an answer, but also provide an explanation of what your code does and how it solves the problem of the question. Answers with an explanation are usually more helpful and of better quality, and are more likely to attract upvotes.
<|/ c |>
<| c |>
Thanks for your answer. Unfortunately this doesn't solve my problem because I need the port to be accessible from the outside world.
<|/ c |>
<| c |>
This answer doesn't solve your problem. Your code doesn't solve the problem of accessing the port from the outside.
<|/ c |>
<| c |>
I added a working example that uses `socket.gethostname()` to get the host name.
<|/ c |>
<| a tags=python,webserver,sockets |>
<code>
import socket
import http.server

HOST, PORT = "localhost", 8080
Handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer( (HOST, PORT), Handler )
httpd.serve_forever()
</code>
<|/ a dscore=0 |>
<| c |>
Please don't post only code as an answer, but also provide an explanation of what your code does and how it solves the problem of the question